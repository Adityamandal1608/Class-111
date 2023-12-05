import os
import shutil

from_dir="C:/Users/HCL/Downloads"
to_dir="C:/Users/HCL/Desktop/Document_Files"
list_of_files=os.listdir(from_dir)
print(list_of_files)
for filename in list_of_files:
    name,extension=os.path.splitext(filename)
    print(extension)
    