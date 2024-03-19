#!/bin/bash

while [[ $# -gt 0 ]]; do
    parameter="$1"

    case $parameter in
        --input_folder)
            INPUT_FOLDER="$2"
            shift
            shift
            ;;
        --extension)
            EXTENSION="$2"
            shift
            shift
            ;;
        --backup_folder)
            BACKUP_FOLDER="$2"
            shift
            shift
            ;;
        --backup_archive_name)
            BACKUP_ARCHIVE_NAME="$2"
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

find "$INPUT_FOLDER" -name "*.$EXTENSION" -type f | while read file; do
    filename=$(basename -- "$file")
    if [ -f "${BACKUP_FOLDER}/${filename}" ]; then
        index=1
        expected_name="${BACKUP_FOLDER}/${filename%.*}_${index}.${filename##*.}"
        while [ -f "$expected_name" ]; do
            ((index++))
            expected_name="${BACKUP_FOLDER}/${filename%.*}_${index}.${filename##*.}"
        done
        cp "$file" "$expected_name"
    else
        cp "$file" "${BACKUP_FOLDER}/$filename"
    fi
done

tar -czf "${BACKUP_ARCHIVE_NAME}" -C "$(dirname $BACKUP_FOLDER)" "$(basename $BACKUP_FOLDER)"

echo "done"

