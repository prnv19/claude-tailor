#!/usr/bin/env bash
# Workspace lifecycle for /setup, and the preflight of /tailor and /cover.
#
# Usage: engine/scripts/workspace.sh [-C <project-dir>] <command>
#
#   status          Print one key=value line per check (toolchain + workspace
#                   state). Always exits 0, so skills can inject it as context.
#   init            Create workspace/{tailored,build}/ and copy the template in
#                   as workspace/master-resume.tex. Never overwrites a master.
#   backup          Copy the master to workspace/master-resume.backup-<date>.tex,
#                   never overwriting an earlier backup.
#   compile-master  Compile workspace/master-resume.tex into
#                   workspace/build/_master/ and report its page count. The
#                   master may run past one page (it holds everything), so only
#                   a LaTeX error fails this.
#
# The workspace is <project-dir>/workspace. Skills pass -C with the project
# dir because Claude's shell may have cd'd elsewhere. Without -C (or with an
# empty value) it is $CLAUDE_PROJECT_DIR, else the current directory. Never
# the plugin install dir.

set -u

SCRIPTS="$(cd "$(dirname "$0")" && pwd)"
TEMPLATE="$SCRIPTS/../templates/master-resume.tex"
USAGE="Usage: engine/scripts/workspace.sh [-C <project-dir>] status|init|backup|compile-master"

PROJECT="${CLAUDE_PROJECT_DIR:-$PWD}"
if [ "${1:-}" = "-C" ]; then
  [ $# -ge 2 ] || { echo "$USAGE" >&2; exit 2; }
  [ -n "$2" ] && PROJECT="$2"
  shift 2
fi
WORKSPACE="$PROJECT/workspace"
MASTER="$WORKSPACE/master-resume.tex"

# file:package for everything the template's preamble loads (package = the
# TeX Live name to install). The icon font is checked separately, because the
# template takes fontawesome7 when present and falls back to fontawesome5.
LATEX_NEEDS="latexsym.sty:latex fullpage.sty:preprint titlesec.sty:titlesec
marvosym.sty:marvosym color.sty:graphics verbatim.sty:tools enumitem.sty:enumitem
hyperref.sty:hyperref fancyhdr.sty:fancyhdr babel.sty:babel english.ldf:babel-english
tabularx.sty:tools multicol.sty:tools glyphtounicode.tex:pdftex"

find_pdflatex() {
  # MacTeX installs to /Library/TeX/texbin, which non-login shells miss.
  command -v pdflatex 2>/dev/null && return
  [ -x /Library/TeX/texbin/pdflatex ] && echo /Library/TeX/texbin/pdflatex
}

missing_latex() {
  # Print the packages the template needs that kpsewhich can't find, as
  # space-separated TeX Live names. Empty output means everything is there.
  local kpse="$1" pair file pkg found missing=""
  found="$("$kpse" $(for pair in $LATEX_NEEDS; do echo "${pair%%:*}"; done) \
    fontawesome7.sty fontawesome5.sty 2>/dev/null)"
  for pair in $LATEX_NEEDS; do
    file="${pair%%:*}"
    pkg="${pair#*:}"
    case "$found" in *"/$file"*) continue ;; esac
    case " $missing " in *" $pkg "*) ;; *) missing="$missing $pkg" ;; esac
  done
  case "$found" in
    *"/fontawesome7.sty"* | *"/fontawesome5.sty"*) ;;
    *) missing="$missing fontawesome5" ;;
  esac
  echo "${missing# }"
}

status() {
  local pdflatex kpse missing
  pdflatex="$(find_pdflatex)"
  echo "workspace=$WORKSPACE"
  if command -v python3 >/dev/null 2>&1; then echo "python3=ok"; else echo "python3=MISSING"; fi
  if [ -n "$pdflatex" ]; then
    echo "pdflatex=ok"
    kpse="$(dirname "$pdflatex")/kpsewhich"
    if [ -x "$kpse" ]; then
      missing="$(missing_latex "$kpse")"
      if [ -z "$missing" ]; then echo "latex-packages=ok"; else echo "latex-packages=MISSING $missing"; fi
    else
      echo "latex-packages=unknown"
    fi
  else
    echo "pdflatex=MISSING"
    echo "latex-packages=unknown"
  fi
  # Optional: overflow line counts and the plain-text check read PDFs with it.
  if command -v pdftotext >/dev/null 2>&1; then echo "pdftotext=ok"; else echo "pdftotext=MISSING"; fi
  if [ ! -f "$MASTER" ]; then
    echo "master=MISSING"
  elif grep -qE 'PLACEHOLDER CONTENT|you@example\.com|555-555-0100' "$MASTER"; then
    echo "master=placeholder"
  else
    echo "master=ok"
  fi
  # Is the workspace protected from git? Only matters inside a git repo.
  if git -C "$PROJECT" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    if git -C "$PROJECT" check-ignore -q "$MASTER"; then
      echo "gitignore=ok"
    else
      echo "gitignore=MISSING"
    fi
  else
    echo "gitignore=not-a-repo"
  fi
  echo "today=$(date +%Y-%m-%d)"
}

init() {
  if [ ! -d "$PROJECT" ]; then
    echo "No such folder: $PROJECT" >&2
    exit 1
  fi
  mkdir -p "$WORKSPACE/tailored" "$WORKSPACE/build"
  if [ -f "$MASTER" ]; then
    echo "kept: $MASTER (already exists, not overwritten)"
  else
    cp "$TEMPLATE" "$MASTER"
    echo "created: $MASTER (copy of the template, placeholder content)"
  fi
}

backup() {
  local dest
  if [ ! -f "$MASTER" ]; then
    echo "Master not found: $MASTER (nothing to back up)" >&2
    exit 1
  fi
  dest="$WORKSPACE/master-resume.backup-$(date +%Y-%m-%d).tex"
  [ -e "$dest" ] && dest="$WORKSPACE/master-resume.backup-$(date +%Y-%m-%d-%H%M%S).tex"
  cp "$MASTER" "$dest"
  echo "backed up: $dest"
}

compile_master() {
  local pdflatex build pages
  pdflatex="$(find_pdflatex)"
  if [ -z "$pdflatex" ]; then
    echo "pdflatex not found (install MacTeX / TeX Live)" >&2
    exit 1
  fi
  if [ ! -f "$MASTER" ]; then
    echo "Master not found: $MASTER (run init first)" >&2
    exit 1
  fi
  build="$WORKSPACE/build/_master"
  mkdir -p "$build"
  rm -f "$build/master-resume.pdf"
  if ! "$pdflatex" -interaction=nonstopmode -halt-on-error \
      -output-directory="$build" "$MASTER" > "$build/master-resume.stdout" 2>&1; then
    echo "COMPILE FAIL: master-resume.tex, log tail:" >&2
    tail -n 25 "$build/master-resume.log" >&2 2>/dev/null
    exit 1
  fi
  # pdflatex wraps long log lines, so join them before matching.
  pages="$(tr -d '\n' < "$build/master-resume.log" | grep -o 'Output written on [^(]*([0-9]* page' | grep -o '([0-9]*' | tr -d '(')"
  echo "compiled: $build/master-resume.pdf (${pages:-?} page(s))"
}

case "${1:-}" in
  status) status ;;
  init) init ;;
  backup) backup ;;
  compile-master) compile_master ;;
  *)
    echo "$USAGE" >&2
    exit 2
    ;;
esac
