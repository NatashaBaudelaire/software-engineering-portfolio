# File Organization Scripts

This directory contains automation scripts for file organization and management.

## Contents

- **organize_files.py**: Python script that automatically organizes files in a directory by moving them into subdirectories based on their file extensions.

## How to Use

1. Update the `directory_path` variable in `organize_files.py` to point to your target directory
2. Run the script:
   ```bash
   python organize_files.py
   ```

## Customization

You can customize the file organization by modifying the `extensions` dictionary in the script to add new file types and destination directories.

## Supported File Types

By default, the script supports:
- PDF files → Files directory
- JPG/PNG images → Images directory
- XLSX spreadsheets → Spreadsheets directory

## Notes

- The script creates destination directories if they don't exist
- Files are moved, not copied
- The script skips directories and only processes files
- Ensure you have appropriate permissions for the source and destination directories
