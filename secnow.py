__all__ = ["secnow"]

import time

def secnow():
    return time.time() % (24 * 3600)
