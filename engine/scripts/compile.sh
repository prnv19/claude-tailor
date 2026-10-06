#!/usr/bin/env bash
# Canonical compile for tailored resumes and cover letters.
#
# Usage: engine/scripts/compile.sh [-C <project-dir>] <Company> <Role> [tex-name ...]
#
# - Compiles resume.tex (and cover-letter.tex if present) unless specific
#   tex names are given.
# - All pdflatex scratch (.aux/.log/.out) goes to workspace/build/<Company>/<Role>/.
# - Copies the final PDF next to its .tex in workspace/tailored/<Company>/<Role>/.
# - Removes any stray scratch files from the tailored dir.
# - Runs check_resume.py (mechanical Hard Constraint checks) at the end.
#
# Exit code is non-zero if any compile or constraint check fails.
#
# The workspace is <project-dir>/workspace: -C if given, else
# $CLAUDE_PROJECT_DIR, else the current directory. Never the plugin install
# dir, because scripts may run from the read-only plugin cache.

set -u

SCRIPTS="$(cd "$(dirname "$0")" && pwd)"
USAGE="Usage: engine/scripts/compile.sh [-C <project-dir>] <Company> <Role> [tex-name ...]"

PROJECT="${CLAUDE_PROJECT_DIR:-$PWD}"
if [ "${1:-}" = "-C" ]; then
  [ $# -ge 2 ] || { echo "$USAGE" >&2; exit 2; }
  [ -n "$2" ] && PROJECT="$2"
  shift 2
fi
WORKSPACE="$PROJECT/workspace"

if [ $# -lt 2 ]; then
  echo "$USAGE" >&2
  exit 2
fi

COMPANY="$1"
ROLE="$2"
shift 2
# Slugs become folder names that pdflatex and the shell both see, so they hold
# letters (accented ones too), digits, "-", "_", and "." only. "%" and "~"
# break pdflatex, "$" and backticks expand inside double quotes, and "/"
# or a leading "." could leave the workspace.
for slug in "$COMPANY" "$ROLE"; do
  case "$slug" in
    "" | .* | *[![:alnum:]._-]*)
      echo "Invalid Company/Role slug '$slug': use letters, digits, and hyphens" >&2
      echo "(spaces become hyphens, '&' becomes 'and', drop other punctuation)." >&2
      exit 2
      ;;
  esac
done

TAILORED="$WORKSPACE/tailored/$COMPANY/$ROLE"
BUILD="$WORKSPACE/build/$COMPANY/$ROLE"

# pdflatex may not be on PATH in non-login shells (MacTeX installs to
# /Library/TeX/texbin via /etc/paths.d, which only login shells pick up).
PDFLATEX="$(command -v pdflatex || true)"
if [ -z "$PDFLATEX" ] && [ -x /Library/TeX/texbin/pdflatex ]; then
  PDFLATEX=/Library/TeX/texbin/pdflatex
fi
if [ -z "$PDFLATEX" ]; then
  echo "pdflatex not found (install MacTeX / TeX Live, or add /Library/TeX/texbin to PATH)" >&2
  exit 1
fi

if [ ! -d "$TAILORED" ]; then
  echo "No such tailored dir: $TAILORED" >&2
  echo "Check the Company/Role slugs, or pass -C with the folder that holds workspace/." >&2
  exit 1
fi

if [ $# -gt 0 ]; then
  FILES="$*"
else
  FILES=""
  for f in resume.tex cover-letter.tex; do
    [ -f "$TAILORED/$f" ] && FILES="$FILES $f"
  done
fi

if [ -z "${FILES// /}" ]; then
  echo "Nothing to compile in $TAILORED" >&2
  exit 1
fi

mkdir -p "$BUILD"
STATUS=0

for f in $FILES; do
  stem="${f%.tex}"
  # Delete last run's PDFs first so a failed compile can never leave a stale
  # PDF behind for the checker (or the user) to mistake for the new one.
  rm -f "$BUILD/$stem.pdf" "$TAILORED/$stem.pdf"
  if "$PDFLATEX" -interaction=nonstopmode -halt-on-error \
      -output-directory="$BUILD" "$TAILORED/$f" > "$BUILD/$stem.stdout" 2>&1; then
    cp "$BUILD/$stem.pdf" "$TAILORED/$stem.pdf"
    echo "compiled: $TAILORED/$stem.pdf"
  else
    echo "COMPILE FAIL: $f, log tail:" >&2
    tail -n 25 "$BUILD/$stem.log" >&2 2>/dev/null || cat "$BUILD/$stem.stdout" >&2
    STATUS=1
  fi
done

# Never leave scratch in tailored/
rm -f "$TAILORED"/*.aux "$TAILORED"/*.log "$TAILORED"/*.out 2>/dev/null

if [ $STATUS -ne 0 ]; then
  echo "FAIL: LaTeX compile failed, skipped constraint checks (no PDF produced)" >&2
  exit $STATUS
fi

python3 "$SCRIPTS/check_resume.py" -C "$PROJECT" "$COMPANY" "$ROLE" --build-dir "$BUILD" || STATUS=1

exit $STATUS
