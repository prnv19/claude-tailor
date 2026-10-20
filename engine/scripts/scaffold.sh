#!/usr/bin/env bash
# Scaffold a tailored role folder from the master resume.
#
# Usage: engine/scripts/scaffold.sh [-C <project-dir>] <Company> <Role>
#
# Creates workspace/applications/<Company>/<Role>/ and copies
# workspace/master-resume.tex in as resume.tex, so the agent starts
# from a byte-identical preamble (Hard Constraint 8 passes by
# construction). The agent then regenerates each entry's
# \resumeItemListStart ... \resumeItemListEnd block from master's facts
# (/tailor step 5) and leaves everything outside those lists untouched.
#
# Refuses to overwrite an existing resume.tex.
#
# The workspace is <project-dir>/workspace: -C if given, else
# $CLAUDE_PROJECT_DIR, else the current directory. Never the plugin install
# dir, because scripts may run from the read-only plugin cache.

set -u

USAGE="Usage: engine/scripts/scaffold.sh [-C <project-dir>] <Company> <Role>"

PROJECT="${CLAUDE_PROJECT_DIR:-$PWD}"
if [ "${1:-}" = "-C" ]; then
  [ $# -ge 2 ] || { echo "$USAGE" >&2; exit 2; }
  [ -n "$2" ] && PROJECT="$2"
  shift 2
fi
WORKSPACE="$PROJECT/workspace"

if [ $# -ne 2 ]; then
  echo "$USAGE" >&2
  exit 2
fi

COMPANY="$1"
ROLE="$2"
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
MASTER="$WORKSPACE/master-resume.tex"
DEST="$WORKSPACE/applications/$COMPANY/$ROLE"

if [ ! -f "$MASTER" ]; then
  echo "Master not found: $MASTER" >&2
  echo "Run /setup first, or pass -C with the folder that holds workspace/." >&2
  exit 1
fi

if [ -f "$DEST/resume.tex" ]; then
  echo "Refusing to overwrite existing $DEST/resume.tex" >&2
  echo "Delete it first if you really want to re-scaffold." >&2
  exit 1
fi

mkdir -p "$DEST"
cp "$MASTER" "$DEST/resume.tex"
echo "scaffolded: $DEST/resume.tex (copy of master-resume.tex)"
echo "next: regenerate the bullet lists only (preamble and subheadings stay"
echo "      verbatim), save jd.md, run compile.sh \"$COMPANY\" \"$ROLE\","
echo "      then write resume-diff.md last, once the PDF is final."
