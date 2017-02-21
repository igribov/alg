'''
'''
def countKeysEqual(A, n, m):
    equals = { i : 0 for i in m }
    for i in range(n):
        key = A[i]
        equals[key]+=1
    return equals

def countKeysLess(equal, m):
    less = { i : 0 for i in m }
    for j in m:
        previos = [i for i in m if i < j]
        if previos:
            prev_j = previos[-1]
            less[j] = less[prev_j] + equal[prev_j]
    return less

def rearrange(A, less, n, m):
    B = [0] * n
    Next = { i : 0 for i in m }
    for j in m:
        Next[j] = less[j]
    
    for i in range(0,n):
        key = A[i]
        index = Next[key]
        B[index] = A[i]
        Next[key]+=1
    return B

def countingSort(A,n,m):
    equal = countKeysEqual(A, n, m)
    less = countKeysLess(equal, m)
    return rearrange(A, less, n, m)

def improveCountingSort(A):
    n = len(A)
    m = set(A)
    equal = countKeysEqual(A, n, m)
    less = countKeysLess(equal, m)
    return rearrange(A, less, n, m)
    
if __name__ == '__main__':
    A = [4,1,5,0,7,1,6,5,1,5,3,3,2,4,5,3,2,5,3,3,9]
    res = improveCountingSort(A)
    print(res)
    
