__all__ = ["basen"]

def basen(n, alphabet):
   div, mod = divmod(n, len(alphabet))
   if div > 0:
      return basen(div, alphabet) + alphabet[mod]
   return alphabet[mod]
