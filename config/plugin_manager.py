import os, sys, json, shutil, subprocess, time
import utils


# Use %USERNAME% in plugin jsons to get the current user

class PluginManager:

    def __init__(self):
        self.root = "\\".join((__file__.split("\\")[:-2]))
        self.plugin_dir = "\\".join([self.root, "plugins"])

        # TO DO: Decouple this self.supported variable from hard coded <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        self.supported = ["houdini", "maya", "nuke", "mari", "zbrush"]

    # Function for getting 2 sorted lists, 1 for Plugins and the other for Lazy Load Plugins
    # TO DO: implement a proper way to figure out if something has been loaded after being called as lazy <<<<<<<<<<<<<<
    # TO DO: implement method of writing to/creating new plugin Json files through project manager <<<<<<<<<<<<<<<<<<<<<

    # Get plugins auto sorts priority, so don't need to implement priority sorting into exec function

    def get_plugins(self):

        plugin_priority = {}
        lazy_priority = {}
        plugins = []
        lazy_plugins = []

        # Looping through plugins directory

        for plugin in os.listdir(self.plugin_dir):
            if plugin == "template.json":
                continue

            plugin_path = "\\".join([self.plugin_dir, plugin])
            plugin_data = utils.load_json(plugin_path)

            # Getting priority, base priority is 50

            try:
                priority = plugin_data["priority"]
            except:
                priority = 50

            # Getting Lazy, Lazy off by default

            try:
                lazy = plugin_data["lazy"]
                if lazy:
                    lazy_priority[plugin_path] = priority
                    lazy_plugins.append(plugin_path)
                    continue
            except:
                lazy = False

            plugin_priority[plugin_path] = priority
            plugins.append(plugin_path)

        # Sorting order of plugins based on the priority in the dictionaries above using Lambda

        active_plugins = sorted(plugins, key=lambda target: plugin_priority[target], reverse=True)
        lazy_plugins = sorted(lazy_plugins, key=lambda target: lazy_priority[target], reverse=True)

        return active_plugins, lazy_plugins

    @staticmethod
    def exec_plugins(plugins_list):

        for plugin in plugins_list:
            plugin_data = utils.load_json(plugin)

            # TO DO: Separate this sets list from Python script rather than hard coding <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

            set = ["name", "package", "pref_source", "pref_destination", "tool_source", "tool_destination",
                   "package_destination", "script", "run", "overwrite"]

            fixed_plugin_data = {}
            for item in set:
                try:
                    fixed_plugin_data[item] = plugin_data[item]
                except:
                    fixed_plugin_data[item] = None

            # TO DO: set a checking system to make sure scripts is a list of strings <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

            if fixed_plugin_data["run"] and isinstance(fixed_plugin_data["scripts"], list):

                for s in fixed_plugin_data["scripts"]:
                    if isinstance(s, str):
                        subprocess.call(s, shell=False)

            # checks if a valid package and package destination exists, and attempts to copy if both are found.

            if isinstance(fixed_plugin_data["package_destination"], str) \
                and os.path.isdir(fixed_plugin_data["package_destination"]):

                if isinstance(fixed_plugin_data["package"], str) and os.path.isfile(fixed_plugin_data["package"]):
                    try:
                        shutil.copy(fixed_plugin_data["package"], fixed_plugin_data["package_destination"])
                    except:
                        print("Failed: Check if package: {0} : already exists at target location."
                              .format(fixed_plugin_data["package"]))

            # Checks if Tool source and destination exist, and if so runs copy full dir function.

            if isinstance(fixed_plugin_data["tool_destination"], str) \
                    and os.path.isdir(fixed_plugin_data["tool_destination"]):
                if isinstance(fixed_plugin_data["tool_source"], str) and \
                        os.path.isdir(fixed_plugin_data["tool_source"]):
                    utils.copy_full_dir(fixed_plugin_data["tool_source"], fixed_plugin_data["tool_destination"],
                                        fixed_plugin_data["overwrite"])

            # Checks if Pref source and destination exist, and if so runs copy full dir function.

            if isinstance(fixed_plugin_data["pref_destination"], str) \
                    and os.path.isdir(fixed_plugin_data["pref_destination"]):
                if isinstance(fixed_plugin_data["pref_source"], str) and \
                        os.path.isdir(fixed_plugin_data["pref_source"]):
                    utils.copy_full_dir(fixed_plugin_data["pref_source"], fixed_plugin_data["pref_destination"],
                                        fixed_plugin_data["overwrite"])


