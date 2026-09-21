#!/usr/bin/env zsh
set -euo pipefail

script_dir=${0:A:h}
repo_root=${script_dir:h}
materials_dir="$repo_root/materials"
sources_dir="$repo_root/sources"

command -v curl >/dev/null || { print -u2 '缺少 curl'; exit 1; }
command -v rg >/dev/null || { print -u2 '缺少 rg'; exit 1; }
command -v ffmpeg >/dev/null || { print -u2 '缺少 ffmpeg'; exit 1; }

mkdir -p "$materials_dir" "$sources_dir"

index_file="$sources_dir/SOURCES.csv"
print -r -- 'level,period,set,page_url,paper_url,answer_url,audio_url,paper_path,answer_path,audio_path,verification_note' > "$index_file"

download_file() {
  local url=$1
  local destination=$2
  local partial="${destination}.part"

  if [[ -s "$destination" ]]; then
    print -- "保留已有文件：${destination#$repo_root/}"
    return
  fi

  curl --fail --location --retry 3 --retry-all-errors \
    --connect-timeout 20 --max-time 300 \
    --output "$partial" "$url"
  mv "$partial" "$destination"
}

for level_slug in cet4 cet6; do
  if [[ "$level_slug" == cet4 ]]; then
    level_name=CET4
  else
    level_name=CET6
  fi

  for session in 2024-12 2025-06 2025-12 2026-06; do
    year=${session%%-*}
    month=${session##*-}
    period="${year}/${month#0}"

    for set_number in 1 2 3; do
      page_url="https://english-exam.lazynote.cn/${level_slug}/paper/${session}-${set_number}/"
      print -- "读取：$level_name $period 第${set_number}套"

      page_html=$(curl --fail --location --retry 3 --retry-all-errors \
        --connect-timeout 20 --max-time 120 --silent --show-error "$page_url")

      pdf_urls=(${(f)"$(print -r -- "$page_html" \
        | rg -o 'https://downloads\.lazynote\.cn/[^" ]+\.pdf' \
        | awk '!seen[$0]++' \
        | head -2)"})

      if (( ${#pdf_urls[@]} != 2 )); then
        print -u2 -- "未找到完整的整卷 PDF 与解析 PDF：$page_url"
        exit 1
      fi

      destination_dir="$materials_dir/$level_name/$year/$month/第${set_number}套"
      mkdir -p "$destination_dir"

      paper_path="$destination_dir/真题.pdf"
      answer_path="$destination_dir/答案解析.pdf"
      download_file "$pdf_urls[1]" "$paper_path"
      download_file "$pdf_urls[2]" "$answer_path"

      audio_url=$(print -r -- "$page_html" \
        | rg -o 'https://listening\.lazynote\.cn/[^"& ]+/index\.m3u8' \
        | head -1 || true)
      audio_path=''
      verification_note='整卷真题与第三方参考解析已下载'

      if [[ -n "$audio_url" ]]; then
        audio_file="$destination_dir/听力.mp3"
        if [[ ! -s "$audio_file" ]]; then
          print -- "转存听力：${audio_file#$repo_root/}"
          ffmpeg -nostdin -hide_banner -loglevel error -y \
            -i "$audio_url" -vn -c:a libmp3lame -b:a 128k -f mp3 "${audio_file}.part"
          mv "${audio_file}.part" "$audio_file"
        else
          print -- "保留已有文件：${audio_file#$repo_root/}"
        fi
        audio_path=${audio_file#$repo_root/}
        verification_note='整卷真题、第三方参考解析与公开听力已下载'
      else
        verification_note='整卷真题与第三方参考解析已下载；来源页未提供独立听力'
      fi

      paper_rel=${paper_path#$repo_root/}
      answer_rel=${answer_path#$repo_root/}
      print -r -- \
        "\"$level_name\",\"$period\",\"第${set_number}套\",\"$page_url\",\"$pdf_urls[1]\",\"$pdf_urls[2]\",\"$audio_url\",\"$paper_rel\",\"$answer_rel\",\"$audio_path\",\"$verification_note\"" \
        >> "$index_file"
    done
  done
done

(
  cd "$repo_root"
  find materials -type f -print0 | sort -z | xargs -0 shasum -a 256 > sources/SHA256SUMS
)

print -- "下载完成。"
