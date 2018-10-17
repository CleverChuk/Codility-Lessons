# 1. BinaryGap
# Find longest sequence of zeros in binary representation of an integer.


def BinaryGap(N):
    # write your code in Python 3.6
    flag = False
    gap = 0
    num_1 = 0
    count = 0
    f = False
    while N > 0:
        r = N % 2
        N //= 2

        flag = r == 1 and not flag

        if r == 0:
            count += 1
        else:
            if not f:
                count = 0
                f = not f
            num_1 += 1
            if num_1 > 2:
                num_1 = 2

        if flag and num_1 == 2:
            gap = max(gap, count)
            count = 0
            num_1 = 1
    return gap
