from PySide6.QtCore import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
import os, sys, json, shutil, subprocess, time


# THIS NEEDS TO BE FIXED LATER, CURRENTLY NOT USED <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Create Class and Super for feeding into main.py functions

# Loading UI QtDesigner file and connecting up all the buttons
def load_main_window(file_path):
    loader = QUiLoader()
    file = QFile(file_path)

    file.open(QFile.ReadOnly)
    window = loader.load(file)
    file.close()

    # Connect Buttons to run functions

    window.load_all.clicked.connect(self.run_load_all)
    window.load_tools.clicked.connect(self.run_load_tools)
    window.load_prefs.clicked.connect(self.run_load_prefs)
    window.save_prefs.clicked.connect(self.run_save_prefs)
    window.load_tik.clicked.connect(self.run_load_tik)
    window.backup_project.clicked.connect(self.run_backup_project)

    self.window = window
    return self.window
