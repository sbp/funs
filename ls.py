__all__ = ["ls"]

import os

def ls(directory=None):
    if directory is None:
        directory = os.getcwd()
    return os.listdir(directory)
