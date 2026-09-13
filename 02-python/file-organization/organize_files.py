import os
import shutil

# Path of the directory we want to organize
# Update this path to your target directory
directory_path = r"C:\Users\YourUsername\Documents\Project"

print(os.listdir(directory_path))

# Dictionary mapping each file extension to its destination directory
extensions = {"pdf": "Files", "jpg": "Images", "png": "Images", "xlsx": "Spreadsheets"}

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
