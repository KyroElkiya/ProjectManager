from utils import startup_utils
import webbrowser


def main(root: str):

    data = startup_utils.load_config_users_json(root, "browser")
    browser = f'"{data["browser"]}" %s'
    webbrowser.get(browser).open(data["website"])


