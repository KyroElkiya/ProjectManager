import os, sys, json, subprocess, shutil, time


# Function to read Json files
def load_json(config):
    with open(config) as json_data:
        data = json.load(json_data)
        json_data.close()

    return data
