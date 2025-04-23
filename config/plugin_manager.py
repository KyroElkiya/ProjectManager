import os, sys, json, shutil, subprocess, time
import utils


# Use %USERNAME% in plugin jsons to get the current user

class PluginManager:

    def __init__(self):
        self.root = "\\".join((__file__.split("\\")[:-2]))
        self.plugin_dir = "\\".join(self.root, "plugins")

    # Function for getting 2 sorted lists, 1 for Plugins and the other for Lazy Load Plugins
    # TO DO: implement a proper way to figure out if something has been loaded after being called as lazy <<<<<<<<<<<<<<
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

        plugins = sorted(plugins, key=lambda target: plugin_priority[target], reverse=True)
        lazy_plugins = sorted(lazy_plugins, key=lambda target: lazy_priority[target], reverse=True)

        return plugins, lazy_plugins

