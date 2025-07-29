import os
import sys
import helpers

def load_config_users_json(root: str, filename: str):

    username = os.getlogin()
    
    target_json = f"{root}/config/{username}/{filename}.json"
    fallback_json = f"{root}/config/default/{filename}.json"
    
    if os.path.exists(target_json):
        return helpers.load_json(target_json)
    
    else:
        return helpers.load_json(fallback_json)
