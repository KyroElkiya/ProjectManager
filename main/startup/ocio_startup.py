import subprocess
from utils import helpers
def main(root):

    ocio_json = f"{root}/config/default/ocio.json"
    
    data = helpers.load_json(ocio_json)

