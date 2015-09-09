__all__ = ["pad"]

def pad(text, n, zero="0"):
    return text.rjust(n, zero)
