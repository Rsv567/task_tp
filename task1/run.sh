#!/bin/bash

while [[ $# -gt 0 ]]; do
    parametr="$1"

    case $parametr in
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

mkdir -p "${INPUT_FOLDER}/${BACKUP_FOLDER}"

find "$INPUT_FOLDER" -name "*.$EXTENSION" -type f | while read file; do
    filename=$(basename -- "$file")
    if [ -f "${INPUT_FOLDER}/${BACKUP_FOLDER}/${filename}" ]; then
        index=1
        while [ -f "${INPUT_FOLDER}/${BACKUP_FOLDER}/${filename%.*}_${index}.${filename##*.}" ]; do
            ((index++))
        done
        cp "$file" "${INPUT_FOLDER}/${BACKUP_FOLDER}/${filename%.*}_${index}.${filename##*.}"
    else
        cp "$file" "${INPUT_FOLDER}/${BACKUP_FOLDER}/$filename"
    fi
done

tar -czf "${INPUT_FOLDER}/${BACKUP_ARCHIVE_NAME}" -C "${INPUT_FOLDER}" "${BACKUP_FOLDER}"

echo "done"
