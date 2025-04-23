from PySide6.QtCore import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
import os, sys, shutil, subprocess, time

# TO DO: ADD CUSTOM QT UI, CONVERT TO CLASS

ignore_pattern = ""

# Depth first search algorithm for finding all sub files in a given directory
# Takes a .Json file with a list of file extensions to bypass

# IMPORTANT SPEED UP IN DFS TARGET FILES, RESEARCH LATER <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def dfs_target_files(root):

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
                # RESEARCH THIS LATER! ^^^^^^ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

                match len(os.listdir(path)):
                    case 0:
                        files.append(path)
                    case _:
                        additional_files = dfs_target_files(path)

                        for f in additional_files:
                            files.append(f)
            case False:
                keep = True
                for ext in ignore_pattern:

                    if dir.endswith(ext) == True:
                        keep = False

                if keep == True:
                    files.append(path)
    return files

# Backup Script for Project, Only backs up scene files due to dfs target files script
# ADD QT PROGRESS BAR
# Must be a way to optimise file copying, maybe through multithreading? RESEARCH LATER <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
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

