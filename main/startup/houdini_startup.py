from utils import file_utils, startup_utils
import shutil

def main(root: str):
    
    # Load data from houdini.json

    data = startup_utils.load_config_users_json(root, "houdini")

    # Copy package file to houdini package directory
    
    file_utils.copy_and_replace(data["package"], data["houdini_package_dir"])
    
    # Grab all preferences files from custom preferences directory and copy them to houdini preferences directory 

    custom_prefs = file_utils.list_subfiles(data["custom_preferences_dir"])
    file_utils.multi_copy_and_replace(custom_prefs, data["houdini_preferences_dir"])
    

