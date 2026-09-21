#!/usr/bin/env zsh
set -euo pipefail

script_dir=${0:A:h}
repo_root=${script_dir:h}

cd "$repo_root"

expected_sets=24
paper_count=$(find materials -type f -name '真题.pdf' | wc -l | tr -d ' ')
answer_count=$(find materials -type f -name '答案解析.pdf' | wc -l | tr -d ' ')
audio_count=$(find materials -type f -name '听力.mp3' | wc -l | tr -d ' ')

[[ "$paper_count" == "$expected_sets" ]] || { print -u2 "真题数量错误：$paper_count/$expected_sets"; exit 1; }
[[ "$answer_count" == "$expected_sets" ]] || { print -u2 "解析数量错误：$answer_count/$expected_sets"; exit 1; }

while IFS= read -r -d '' pdf; do
  file "$pdf" | rg -q 'PDF document' || { print -u2 "不是有效 PDF：$pdf"; exit 1; }
  if command -v pdfinfo >/dev/null; then
    pages=$(pdfinfo "$pdf" | awk -F: '/^Pages:/ {gsub(/ /, "", $2); print $2}')
    [[ -n "$pages" && "$pages" -gt 0 ]] || { print -u2 "PDF 页数异常：$pdf"; exit 1; }
  fi
done < <(find materials -type f -name '*.pdf' -print0)

while IFS= read -r -d '' audio; do
  file "$audio" | rg -qi 'audio|mpeg|mp3' || { print -u2 "不是有效音频：$audio"; exit 1; }
  if command -v ffprobe >/dev/null; then
    duration=$(ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 "$audio")
    awk -v value="$duration" 'BEGIN { exit !(value > 60) }' || { print -u2 "音频时长异常：$audio"; exit 1; }
  fi
done < <(find materials -type f -name '*.mp3' -print0)

shasum -a 256 -c sources/SHA256SUMS >/dev/null

print -- "验证通过：$paper_count 套真题、$answer_count 份解析、$audio_count 个听力文件。"

