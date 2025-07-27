import os
import shutil

source = "source_folder"
destination = "jpg_files"

if not os.path.exists(destination):
    os.makedirs(destination)

for file in os.listdir(source):
    if file.endswith(".jpg"):
        shutil.move(os.path.join(source, file), os.path.join(destination, file))

print("✅ All .jpg files moved successfully.")
