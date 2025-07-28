import os
from startup import houdini_startup

def main():
    
    root = os.path.dirname(__file__)
    houdini_startup.main(root)
    

main()
