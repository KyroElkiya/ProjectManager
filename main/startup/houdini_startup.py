from utils import helpers, file_utils
import shutil

def main(root: str):
    
    # Load data from houdini.json
    # Need to automate getting current user, rather than using default constantly <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    houdini_json = f"{root}/config/default/houdini.json"
    data = helpers.load_json(houdini_json)

    # Copy package file to houdini package directory
    
    file_utils.copy_and_replace(data["package"], data["houdini_package_dir"])
    
    # Grab all preferences files from custom preferences directory and copy them to houdini preferences directory 

    custom_prefs = file_utils.list_subfiles(data["custom_preferences_dir"])
    file_utils.multi_copy_and_replace(custom_prefs, data["houdini_preferences_dir"])
    

