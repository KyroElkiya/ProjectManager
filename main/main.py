import os
from startup import houdini_startup

def main():
    
    root = os.path.dirname(__file__)
    # startup(root)
    

def startup(root: str):

    houdini_startup.main(root)


main()
