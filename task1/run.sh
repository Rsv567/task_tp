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


mkdir -p "${BACKUP_FOLDER}"

find "$INPUT_FOLDER" -type f | while read file; do
    filename=$(basename -- "$file")
    if [ -f "${BACKUP_FOLDER}/${filename}" ]; then
        index=1
        while [ -f "${BACKUP_FOLDER}/${filename%.*}_${index}.${filename##*.}" ]; do
            ((index++))
        done
        cp "$file" "${BACKUP_FOLDER}/${filename%.*}_${index}.${filename##*.}"
    else
        cp "$file" "${BACKUP_FOLDER}/$filename"
    fi
done

tar -czf "${BACKUP_ARCHIVE_NAME}" -C "$(dirname $BACKUP_FOLDER)" "$(basename $BACKUP_FOLDER)"

echo "done"

