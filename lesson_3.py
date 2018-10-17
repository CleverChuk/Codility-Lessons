def PermMissingElem(A):
    # write your code in Python 3.6
    A = sorted(A)
    if len(A) == 0 or (len(A) == 1 and A[0] != 1):
        return 1

    if len(A) == 1 and A[0] == 1:
        return 2

    if A[0] != 1:
        return 1

    n = len(A) - 1

    for i in range(n):
        if A[i+1] - A[i] != 1:
            return A[i] + 1

    return A[-1]+1


def FrogJmp(X, Y, D):
    # write your code in Python 3.6
    from math import ceil
    if X - Y == 1:
        return 1
    if D == 0:
        return D

    return ceil(abs(Y-X)/D)


def TapeEquilibrium(A):
    # write your code in Python 3.6
    p = len(A) - 1
    lsum = 0
    rsum = sum(A)
    
    m = 20000
    for i in range(p):
        lsum += A[i]
        rsum -= A[i]
        diff = abs(lsum - rsum)
        
        m = min(m, diff)

    return m
