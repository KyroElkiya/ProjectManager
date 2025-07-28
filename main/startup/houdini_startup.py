from utils import helpers
import shutil

def main(root: str):
    
    houdini_json = f"{root}/config/template_user/houdini.json"
    data = helpers.load_json(houdini_json)

    shutil.copy(data["package"], data["houdini_package_dir"])
    
    

