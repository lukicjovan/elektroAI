import os
import importlib

PLUGIN_FOLDER = "plugins"

def get_plugins():
    plugins = []
    if not os.path.exists(PLUGIN_FOLDER):
        return plugins

    for filename in os.listdir(PLUGIN_FOLDER):
        if filename.endswith(".py") and not filename.startswith("__"):
            module_name = filename[:-3]
            plugins.append(module_name)
    return plugins

def run_plugin(plugin_name, *args, **kwargs):
    try:
        module_path = f"{PLUGIN_FOLDER}.{plugin_name}"
        plugin_module = importlib.import_module(module_path)
        if hasattr(plugin_module, "run"):
            return plugin_module.run(*args, **kwargs)
        else:
            raise AttributeError(f"Plugin '{plugin_name}' nema funkciju 'run'")
    except Exception as e:
        print(f"[GREŠKA] Plugin '{plugin_name}' nije uspešno pokrenut: {e}")
        return None