"""
nuke_utils.py

This module provides utility functions for working with Nuke, a node-based
digital compositing application.
"""

import nuke


def create_camera():
    """
    Create a new Camera2 node in the Nuke node graph.

    Returns:
        nuke.Node: A newly created Camera2 node.
    """
    camera = nuke.createNode("Camera2")
    return camera