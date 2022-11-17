import numpy as np

def betterIntegerType(n):
    n2 = n**2
    if n2 < 2**8:
        return np.uint8
    elif n2 < 2**16:
        return np.uint16
    elif n2 < 2**32:
        return np.uint32
    elif n2 < 2**64:
        return np.uint64
    else:
        return int

def makeMagicSquare(n):
    square =  np.zeros((n,n), dtype=betterIntegerType(n))
    # TODO: fill magic square
    return square
