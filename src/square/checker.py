import numpy as np

def magiSum(n: np.integer) -> np.integer:
    return n * (n**2 + 1) // 2

def isSquare(array: np.ndarray) -> bool:
    if len(array.shape) != 2:
        return False
    n,m = array.shape
    return n == m

def allPresent(square):
    n, _ = square.shape
    n2 = n**2
    check = { v: False for v in range(1, n2+1)}
    for v in np.nditer(square):
        if not (1 < v < n2):
            return False
        check[v] ^= True
    return all(check.values())

def isMagicSquare(square: np.ndarray) -> bool:
    assert isSquare(square)
    n, _ = square.shape
    sm = magiSum(n)
    return (
        np.all(square.sum(axis=0) == sm)
        and np.all(square.sum(axis=1) == sm)
        and (square.diagonal().sum() == sm)
        and (square[::-1].sum() == sm)
        # and allPresent(square)
    )
