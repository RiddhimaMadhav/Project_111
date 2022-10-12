import os
import shutil

from_dir = "C:/Users/ashis/Downloads/Here"
to_dir = "C:/Users/ashis/OneDrive/Documents/Document_Files"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)