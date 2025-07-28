import os
import shutil

def list_subfiles(directory: str):
    
    subfiles = []

    for child in os.listdir(directory):
        path = os.path.join(directory, child)
        
        if os.path.isfile(path):
            subfiles.append(path)
    
    return subfiles


def copy_and_replace(old_file: str, target_directory: str):

    file_name = os.path.basename(old_file)
    new_file_path = os.path.join(target_directory, file_name)

    if os.path.exists(new_file_path):
        os.remove(new_file_path)
    shutil.copy(old_file, target_directory)


def multi_copy_and_replace(old_files: list[str], target_directory: str):

    for old_file in old_files:
        copy_and_replace(old_file, target_directory)
