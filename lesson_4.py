
def permCheck(A):
    # write your code in Python 3.6
    A = sorted(A)
    prev = None
    count = 0
    for i, v in enumerate(A):
        i += 1
        if prev == v:
            count += 1
        else:
            prev = v
            count = 0

        if count == 2:
            return 0

        if i != v:
            return 0

    return 1


def Buckets(N, Q, B, C):
    # write your code in Python 3.6
    from collections import defaultdict

    n = len(C)
    d = {}

    for i in range(n):
        if B[i] not in d:
            d[B[i]] = defaultdict(int)
            d[B[i]][C[i]] += 1
        else:
            d[B[i]][C[i]] += 1

        if d[B[i]][C[i]] == Q:
            return i

    return -1


def frogRiverOne(X, A):
    # write your code in Python 3.6
    from collections import defaultdict
    pos = defaultdict(int)
    posr = defaultdict(int)

    rsum = 0
    for i in range(1, X+1):
        posr[i] = 1

    for i, p in enumerate(A):
        if posr[p] == 0:
            continue

        if pos[p] != 1:
            rsum += 1

        pos[p] = 1
        if rsum == X:
            return i

    return -1

def maxCounter(N, A):
    # write your code in Python 3.6
    from collections import defaultdict
    d = defaultdict(int)
    m = 0
    mop = 0
      
    for c in A:
       if c == N + 1:
           mop += m
           m = 0
           d = defaultdict(int)
           continue
       
       d[c] += 1
       
       if d[c] > m:
           m = d[c]
           
    r = defaultdict(int) 
    for i in range(1,N+1):
       r[i] = d[i] + mop
    
    
    return tuple(r.values())
