
def cyclicRotation(A, K):
    # write your code in Python 3.6
    if len(A) == 0:
        return A

    for _ in range(K):
        l = A[-1]
        copy = A[:len(A)-1]
        A = [l]+copy
    return A


def OddOccurrencesInArray(A):
    # write your code in Python 3.6
    from collections import defaultdict
    data = defaultdict(int)

    for e in A:
        data[e] += 1

    for k, v in data.items():
        if v % 2 == 1:
            return k
