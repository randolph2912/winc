__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import shutil
import zipfile

def clean_cache():
    cache_dir = "cache"
    if os.path.exists(cache_dir):
        shutil.rmtree(cache_dir)
    os.makedirs(cache_dir)

def cache_zip(zip_file, cache_dir):
    with zipfile.ZipFile(zip_file, "r") as z:
        z.extractall(cache_dir)

def cached_files():
    cache_dir = "cache"
    files = []
    for root, dirs, filenames in os.walk(cache_dir):
        for filename in filenames:
            file_path = os.path.join(root, filename)
            files.append(os.path.abspath(file_path))
    return files

def find_password(files_list):
    for file in files_list:
        if file.endswith('.txt'):
            with open(file, 'r') as f:
                text = f.readlines()
                for line in text:
                    if 'password' in line:
                        password = line.split(' ')[1].strip()
                        return password

files_list = cached_files()
print(find_password(files_list))


