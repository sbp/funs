__all__ = ["plush"]

import sys

def plush(*args, **kargs):
    print(*args, **kargs)
    sys.stdout.flush()
