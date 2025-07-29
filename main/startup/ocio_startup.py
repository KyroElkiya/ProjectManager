import subprocess
from utils import startup_utils


def main(root: str):

    data = startup_utils.load_config_users_json(root, "ocio")

