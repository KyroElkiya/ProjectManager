import os, sys, json, subprocess, shutil, time


# Function to read Json files
def load_json(config: str):
    with open(config) as json_data:
        data = json.load(json_data)
        json_data.close()

    return data


# Function looping through all files/folders in a directory recursively and copies files from source to destination.
def copy_full_dir(src_folder: str, dst_folder: str, overwrite=True):

    for child in os.listdir(src_folder):

        # Setting old and new path variables

        old_path = "\\".join([src_folder, child])
        new_path = old_path.replace(src_folder, dst_folder)

        # Checks if current iteration is a directory, if so recursively loops through that directory

        if os.path.isdir(old_path):
            copy_full_dir(old_path, new_path)
        else:

            # Checks if current folder exists, if it doesn't then the folder is created.

            if not os.path.isdir(dst_folder):
                os.makedirs(dst_folder)

            # Checks if overwriting files is true, if not, skips over file if already exists

            if not overwrite:
                if os.path.exists(new_path):
                    pass
                else:
                    shutil.copyfile(old_path, new_path)
                    print("{0} successfully created!".format(new_path))
            else:
                shutil.copyfile(old_path, new_path)
                print("{0} successfully created!".format(new_path))
