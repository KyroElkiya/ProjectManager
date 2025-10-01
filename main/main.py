import os
from startup import houdini_startup, nuke_startup, ocio_startup, zbrush_startup, mari_startup, maya_startup

def main():
    
    root = os.path.dirname(__file__)
    # startup(root)
    

def startup(root: str):

    ocio_startup.main(root)
    houdini_startup.main(root)
    nuke_startup.main(root)
    mari_startup.main(root)
    maya_startup.main(root)
    zbrush_startup.main(root)


main()
