from PySide6.QtCore import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
import os, sys, json, shutil, subprocess, time
from pprint import pprint

# Create Env file with all relevant file paths/variables!


# Defining class
class ProjectManager:

    # Initialise Environment
    def __init__(self, config):
        self.app = QApplication(sys.argv)

    # PyQT Style Sheet for UI: PR it's basically CSS
    @staticmethod
    def style_sheet():
        return ('''
            QWidget {
                font-size: 15px;
                background-color: #222222;
            }
            QPushButton {
                height: 20px;
                color: black;
                background-color: QLinearGradient(
                               x1: 0,
                               x2: 1,
                               y1: 0,
                               y2: 1,
                               stop: 1 #252a34,
                               stop: 0.5 #ff2e63,
                               stop: 0 #ffff11
                );
                border-width: 2px;
                border-color: QLinearGradient(
                               x1: 0,
                               x2: 1,
                               y1: 0,
                               y2: 0,
                               stop: 0 #252a34,
                               stop: 0.5 #ff2e63,
                               stop: 1 #ffff11
                );
                border-style: inset;
                padding: 2px;
            }
            QPushButton:Pressed {
                background-color: QLinearGradient(
                               x1: 0,
                               x2: 1,
                               y1: 0,
                               y2: 1,
                               stop: 1 #342a25,
                               stop: 0.5 #632eff,
                               stop: 0 #11ffff
                );
            }
            QPushButton:hover {
                border-color: #22cccc;
            }
            QLineEdit {
                height: 20px;
                background-color: #eeeeee;
                border-width: 2px;
                border-color: QLinearGradient(
                               x1: 0,
                               x2: 1,
                               y1: 0,
                               y2: 0,
                               stop: 0 #252a34,
                               stop: 0.5 #ff2e63,
                               stop: 1 #ffff11
                );
                border-style: inset;
                padding: 2px;
            }
            QTabWidget {
                color: black;
                background-color: QLinearGradient(
                               x1: 0,
                               x2: 1,
                               y1: 0,
                               y2: 1,
                               stop: 1 #252a34,
                               stop: 0.5 #ff2e63,
                               stop: 0 #ffff11
                );
                border-color: QLinearGradient(
                               x1: 0,
                               x2: 1,
                               y1: 0,
                               y2: 0,
                               stop: 0 #252a34,
                               stop: 0.5 #ff2e63,
                               stop: 1 #ffff11
                );
            }
            QTabBar:Tab:selected {
                color: black;
                background-color: QLinearGradient(
                               x1: 0,
                               x2: 1,
                               y1: 0,
                               y2: 1,
                               stop: 1 #252a34,
                               stop: 0.5 #ff2e63,
                               stop: 0 #ffff11
                );
                border-color: QLinearGradient(
                               x1: 0,
                               x2: 1,
                               y1: 0,
                               y2: 0,
                               stop: 0 #252a34,
                               stop: 0.5 #ff2e63,
                               stop: 1 #ffff11
                );
            }
            ''')

    # Loading UI QtDesigner file and connecting up all the buttons
    def load_ui(self, file_name):
        loader = QUiLoader()
        file = QFile(self.ui + "\\" + file_name)

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

    # Function to run application
    def run(self):
        global window

        window = self.load_ui("ProjectManager_Main_new.ui")
        app = self.app
        window = self.window
        app.setStyleSheet(self.style_sheet())
        window.show()
        app.exec()

    # Function to read Json files
    def load_json(self, config):
        with open(config) as json_data:
            data = json.load(json_data)
            json_data.close()

        return data

    # Depth first search algorithm for finding all sub files in a given directory
    # Takes a .Json file with a list of file extensions to bypass

    # IMPORTANT SPEED UP IN DFS TARGET FILES, RESEARCH LATER <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    def dfs_target_files(self, root):

        files = []

        for dir in os.listdir(root):

            path = "\\".join([root, dir])

            match os.path.isdir(path):
                case True:

                    # Checks if current location being looped is a directory, if True Checks that the directory is empty
                    # If directory isn't empty, runs nested function of self on all children of current directory
                    # If current location is a file, checks if extension in the ignore list
                    # If extension isn't in ignore list, appends the file to a list, returns list on function end

                    # There must be a faster way to check all extensions in the ignore list than a nested for each loop
                    # RESEARCH THIS LATER! ^^^^^^ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

                    match len(os.listdir(path)):
                        case 0:
                            files.append(path)
                        case _:
                            additional_files = self.dfs_target_files(path)

                            for f in additional_files:
                                files.append(f)
                case False:
                    keep = True
                    for ext in self.ignore_pattern:

                        if dir.endswith(ext) == True:
                            keep = False

                    if keep == True:
                        files.append(path)
        return files

    # Custom implementation for loading TIK Manager on Uni PCs due to PCs self wipe on logout
    def load_tik(self):

        user_dir = "C:\\users\\{0}".format(self.user)
        data = self.load_json(self.json + "\\tik_directories.json")

        dst = user_dir + "\\TikManager4"
        target = user_dir + "\\TM4_default"

        if os.path.exists(user_dir + "\\TikManager4") == False:
            shutil.copytree(data["TikManager4"], dst)

        if os.path.exists(target):
            shutil.rmtree(target)

        subprocess.call(data["exe"])

    # Backup Script for Project, Only backs up scene files due to dfs target files script
    # ADD QT PROGRESS BAR
    # Must be a way to optimise file copying, maybe through multithreading? RESEARCH LATER <<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    def backup_project(self):

        dst = QFileDialog.getExistingDirectory()

        if dst != "" and os.path.isdir(dst):

            src = self.project_folder

            children = os.listdir(dst)
            curr_iter = 0

            if len(children) != 0:
                for child in children:
                    if int(child) > curr_iter:
                        curr_iter = int(child)

            curr_iter += 1

            dst = dst + "\\{0:02d}".format(curr_iter)
            print(dst)

            all_files = self.dfs_target_files(src)
            nfiles = len(all_files)

            start = time.time()
            print("Time Started: {0}".format(start))

            prev = time.time()
            for i, f in enumerate(all_files):

                match os.path.isdir(f):
                    case True:
                        target = f.replace(src, dst)
                        if not os.path.exists(target):
                            os.makedirs(target)

                    case False:
                        target = "\\".join(f.replace(src, dst).split("\\")[:-1])

                        if not os.path.exists(target):
                            os.makedirs(target)

                        shutil.copy(f, target)
                        curr = time.time()
                        print("{0} took {1} seconds to complete.".format(target, curr - prev))
                        prev = curr

                print("{i} of {t} complete".format(i=i, t=nfiles))

            end = time.time()

            print("finished in {0:.2f} seconds".format(end - start))

    # Runs Windows PC theme file
    @staticmethod
    def pc_theme(path):
        os.startfile(path)
        time.sleep(1)
        subprocess.call("TASKKILL /F /IM systemSettings.exe")

    # Function for reading project manager environment json file
    def read_env(self):
        env_file = "\\".join(os.path.dirname(os.path.realpath(__file__)), "env\\project_manager_tools.json")
        env = self.load_json()
        self.read_houdini_tools(env)

    # Function for enabling all Houdini tools
    def read_houdini_tools(self, env_file):
        pass

    # Function for enabling all Nuke tools
    def read_nuke_tools(self, env_file):
        pass

    # Function for enabling all Maya tools
    def read_maya_tools(self, env_file):
        pass
