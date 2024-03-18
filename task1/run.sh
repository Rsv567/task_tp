#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

while [[ $# -gt 0 ]]; do
    parametr="$1"

    case $parametr in
        --input_folder)
        INPUT_FOLDER="$2"
        shift
        shift
        ;;
        --backup_folder)
        BACKUP_FOLDER="$SCRIPT_DIR/$2"
        shift
        shift
        ;;
        --backup_archive_name)
        BACKUP_ARCHIVE_NAME="$SCRIPT_DIR/$2"
        shift
        shift
        ;;
        *)
        shift
        ;;
    esac
done

if [ -d "$BACKUP_FOLDER" ]; then
    echo "Backup folder already exists."
else
    mkdir -p "${BACKUP_FOLDER}"
fi

find "$INPUT_FOLDER" -type f | while read file; do
    filename=$(basename -- "$file")
    expected_name="${BACKUP_FOLDER}/${filename}"
    
    if [ -f "$expected_name" ]; then
        index=1
        while [ -f "${expected_name%.*}_${index}.${filename##*.}" ]; do
            ((index++))
            expected_name="${expected_name%.*}_${index}.${filename##*.}"
        done
    fi
    
    cp "$file" "$expected_name"
done

tar -czf "${BACKUP_ARCHIVE_NAME}" -C "$(dirname $BACKUP_FOLDER)" "$(basename $BACKUP_FOLDER)"

echo "done"

