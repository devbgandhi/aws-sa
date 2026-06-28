#!/bin/bash

OUTPUT_DIR="./s3/bashscripts"

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Create 10 files
for i in {1..10}
do
    echo "This is file $i" > "$OUTPUT_DIR/file$i.txt"
    dd if=/dev/urandom of="$OUTPUT_DIR/file$i.txt" bs=1M count=1
done

echo "Created 10 files in $OUTPUT_DIR"