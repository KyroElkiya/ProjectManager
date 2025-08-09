import subprocess
from utils import startup_utils


def main(root: str):
    
    # Loading data from ocio json file in config folder

    data = startup_utils.load_config_users_json(root, "ocio")
    aces_script = data["aces_ocio_env_script"]

    # Running ocio batch script through subprocess
    # Double check this may not fully work when setting OCIO env variable <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    subprocess.run(aces_script)


