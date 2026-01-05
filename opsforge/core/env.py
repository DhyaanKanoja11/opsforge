import os
import platform
import sys
from opsforge import __version__


def get_env_info():
    return {
        "OS": platform.system(),
        "OS Version": platform.release(),
        "Python": platform.python_version(),
        "Executable": sys.executable,
        "CWD": os.getcwd(),
        "OpsForge Version": __version__,
    }
