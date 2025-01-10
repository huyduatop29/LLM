import os
import re
from unidecode import unidecode

folder_path = "E:/Download/DataTest/test2"

def clean_filename(filename,remove_unicode=True , replace_spaces=True):
    if remove_unicode:
        filename = unidecode(filename)

    if replace_spaces:
        filename = filename.replace(" ","_")

    filename = re.sub(r'[^a-zA-Z0-9_.]', '', filename)
    return filename

for filename in os.listdir(folder_path):
    old_file_path = os.path.join(folder_path,filename)
    
    if os.path.isfile(old_file_path):
        new_file_path = os.path.join(folder_path,clean_filename(filename))

        os.rename(old_file_path, new_file_path)
        print(f"Rename {filename} to {clean_filename(filename)}")

print('Rename Sucessfully!')
