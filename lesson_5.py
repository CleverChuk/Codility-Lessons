# Lesson 5
def passinCars(A):
    # write your code in Python 3.6
    num_0s = 0
    total = 0
    
    for i in A:
        if i == 0:
            num_0s += 1
        else:
            total = total + num_0s
        
        if total > 1000000000:
            return -1
    
    return total


def genomicRangeQuery(S, P, Q):
    # write your code in Python 3.6
    ans = []
    
    for q in zip(P,Q):
        if "A" in S[q[0]:q[1]+1]:
            ans.append(1)
        elif "C" in S[q[0]:q[1]+1]:
            ans.append(2)
        elif "G" in S[q[0]:q[1]+1]:
            ans.append(3)
        else:
            ans.append(4)
            
    return ans

def countDiv(A, B, K):
    if A % K == 0
        return B//K - A//K + 1;
        
    return B//K - A//K ;
