#!/usr/bin/env bash
# 编译简历. 用 tectonic(自带 XeLaTeX,自动装包). 用法: bash compile.sh path/to/resume.tex
set -e
TEX="${1:-template/resume_template.tex}"
DIR="$(dirname "$TEX")"; FILE="$(basename "$TEX")"
cd "$DIR"
if command -v tectonic >/dev/null 2>&1; then
  tectonic "$FILE"
else
  xelatex -interaction=nonstopmode "$FILE" && xelatex -interaction=nonstopmode "$FILE"
fi
echo "OK -> $DIR/${FILE%.tex}.pdf"
