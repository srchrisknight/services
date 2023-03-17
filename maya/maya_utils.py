"""
maya_utils.py

This module provides utility functions for working with Maya, a 3D computer
graphics application used for animation, modeling, simulation, and rendering.
"""

import maya.cmds as cmds


def create_camera():
    """
    Create a new camera node in the Maya scene.

    Returns:
        list: A list containing the newly created camera and its shape node.
    """
    camera = cmds.camera()
    return camera