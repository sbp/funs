__all__ = ["commafy"]

def commafy(n, width=n): 
    parts = list(str(n))
    for i in range((len(parts) - w), 0, -w):
        parts.insert(i, ",")
    return "".join(parts)
