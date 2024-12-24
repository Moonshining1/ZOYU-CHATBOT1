import glob
from os.path import basename, dirname, isfile

def __list_all_modules():
    """List all Python modules in the current directory, excluding __init__.py."""
    try:
        mod_paths = glob.glob(dirname(__file__) + "/*.py")
        all_modules = [
            basename(f)[:-3]
            for f in mod_paths
            if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
        ]
        return all_modules
    except Exception as e:
        print(f"Error listing modules: {e}")
        return []

# List and sort all modules
ALL_MODULES = sorted(__list_all_modules())
__all__ = ALL_MODULES + ["ALL_MODULES"]
