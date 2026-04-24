#!/usr/bin/env bash
set -euo pipefail

find data -type f -print0 | while IFS= read -r -d '' path; do
  dir=$(dirname "$path")
  base=$(basename "$path")
  new="$base"

  if [[ "$new" == *"files?file=comext%2F"* ]]; then
    new="${new#files?file=comext%2F}"
  fi

  if [[ "$new" == *"%2F"* ]]; then
    new="${new//%2F/_}"
  fi

  if [[ "$new" == "$base" ]]; then
    continue
  fi

  target="$dir/$new"
  if [[ -e "$target" ]]; then
    echo "WARNING: skipping rename because target exists: $path -> $target"
    continue
  fi

  echo "RENAME: $path -> $target"
  mv "$path" "$target"
done
