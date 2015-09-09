__all__ = ["utf8"]

def utf8(obj):
    return str(obj).encode("utf-8", "replace")
