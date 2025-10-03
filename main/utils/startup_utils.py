import os
import sys
from utils import helpers

# Load config function that attempts to load a user profile, but fallbacks to default if not found.

def load_config_users_json(root: str, filename: str):

    username = os.getlogin()
    
    target_json = f"{root}/config/{username}/{filename}.json"
    fallback_json = f"{root}/config/default/{filename}.json"
    
    if os.path.exists(target_json):
        return helpers.load_json(target_json)
    
    else:
        return helpers.load_json(fallback_json)
