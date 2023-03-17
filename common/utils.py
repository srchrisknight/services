"""
utils.py

This module provides utility functions for detecting the digital content
creation (DCC) environment or operating system in use.
"""

import os
import sys
import platform


def detect_dcc():
    """
    Detect the current DCC environment or operating system based on the
    executable name or platform system.

    Returns:
        str: A string representing the detected environment or operating system
             ("nuke", "maya", "houdini", "os_windows", "os_linux"), or None if
             the environment is not recognized.
    """
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