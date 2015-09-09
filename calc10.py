__all__ = ["calc10"]

import decimal
import re

def calc10(text):
    number = r"(?<![A-Za-z_.-])([+-]?[0-9]+(?:[.][0-9]+)?)(?![A-Za-z_.-])"
    text = re.sub(number, r"decimal.Decimal('\g<1>')", text)
    print(text)
    return eval(text)
