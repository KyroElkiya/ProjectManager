import os
import shutil

# Lists all files (no directories) in the given directory.

def list_subfiles(directory: str):
    
    subfiles = []

    for child in os.listdir(directory):
        path = os.path.join(directory, child)
        
        if os.path.isfile(path):
            subfiles.append(path)
    
    return subfiles

# Takes a file and copies it into target directory, replacing any existing file with the same name.

def copy_and_replace(old_file: str, target_directory: str):

    file_name = os.path.basename(old_file)
    new_file_path = os.path.join(target_directory, file_name)

    if os.path.exists(new_file_path):
        os.remove(new_file_path)
    shutil.copy(old_file, target_directory)

# For each loop wrapper for copy and replace function.

def multi_copy_and_replace(old_files: list[str], target_directory: str):

    for old_file in old_files:
        copy_and_replace(old_file, target_directory)


