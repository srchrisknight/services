import os
import sys
import platform


def detect_dcc():
    executable_name = os.path.basename(sys.executable).lower()

    if "nuke" in executable_name:
        return "nuke"
    elif "maya" in executable_name:
        return "maya"
    elif "houdinifx" in executable_name or "houdini" in executable_name:
        return "houdini"

    if platform.system().lower() == "windows":
        return "os_windows"
    elif platform.system().lower() == "linux":
        return "os_linux"

    return None