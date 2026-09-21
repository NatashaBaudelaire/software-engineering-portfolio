import argparse
import os
import shutil


def organize_files(directory_path: str, extensions: dict) -> None:
    """Organize files in the given directory by extension.

    Args:
        directory_path: Path to the directory to organize.
        extensions: Mapping of file extensions to destination folder names.
    """
    if not os.path.isdir(directory_path):
        raise NotADirectoryError(f"Not a directory: {directory_path}")

    print(f"Organizing files in: {directory_path}")
    print(f"Found: {os.listdir(directory_path)}")

    files = os.listdir(directory_path)

    for file_name in files:
        full_path = os.path.join(directory_path, file_name)

        if os.path.isfile(full_path):
            parts = file_name.split(".")
            extension = parts[-1].lower()

            if extension in extensions:
                destination_directory_name = extensions[extension]
                destination_directory_path = os.path.join(
                    directory_path, destination_directory_name
                )

                if not os.path.exists(destination_directory_path):
                    os.makedirs(destination_directory_path)
                    print(f"Directory created: {destination_directory_name}")

                source = full_path
                destination = os.path.join(destination_directory_path, file_name)

                try:
                    shutil.move(source, destination)
                    print(
                        f"Moved successfully: {file_name} -> {destination_directory_name}"
                    )
                except Exception as e:
                    print(f"Error moving {file_name}: {e}")
            else:
                print(f"Name: {parts[0]}, Type: {extension} -> no rule defined")
        else:
            print(f"{file_name} is a directory, skipping.")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Organize files in a directory by extension."
    )
    parser.add_argument(
        "directory",
        nargs="?",
        default=".",
        help="Directory to organize (default: current directory)",
    )
    args = parser.parse_args()

    extensions = {
        "pdf": "Files",
        "jpg": "Images",
        "png": "Images",
        "xlsx": "Spreadsheets",
    }

    organize_files(args.directory, extensions)


if __name__ == "__main__":
    main()
