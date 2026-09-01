import os
import shutil

# Path of the folder we want to organize
# Update this path to your target directory
folder_path = r"C:\Users\YourUsername\Documents\Project"

print(os.listdir(folder_path))

# Dictionary mapping each file extension to its destination folder
extensions = {
    "pdf": "Files",
    "jpg": "Images",
    "png": "Images",
    "xlsx": "Spreadsheets"
}

files = os.listdir(folder_path)

for file_name in files:
    full_path = os.path.join(folder_path, file_name)

    if os.path.isfile(full_path):
        parts = file_name.split(".")
        extension = parts[-1].lower()

        if extension in extensions:
            destination_folder_name = extensions[extension]
            destination_folder_path = os.path.join(folder_path, destination_folder_name)

            if not os.path.exists(destination_folder_path):
                os.makedirs(destination_folder_path)
                print(f"Folder created: {destination_folder_name}")

            source = full_path
            destination = os.path.join(destination_folder_path, file_name)

            try:
                shutil.move(source, destination)
                print(f"Moved successfully: {file_name} -> {destination_folder_name}")
            except Exception as e:
                print(f"Error moving {file_name}: {e}")
        else:
            print(f"Name: {parts[0]}, Type: {extension} -> no rule defined")
    else:
        print(f"{file_name} is a folder, skipping.")