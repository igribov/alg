'''
'''
def countKeysEqual(A, n, m):
    equals = [0] * (m+1)
    for i in range(n):
        key = A[i]
        equals[key]+=1        
    return equals

def countKeysLess(equal, m):
    less = [0] * (m+1)
    for j in range(1,m+1):
        less[j] = less[j-1] + equal[j-1]
    return less

def rearrange(A, less, n, m):
    B = [0] * n
    Next = [0] * (m+1)
    for j in range(m+1):
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
    m = max(set(A))
    equal = countKeysEqual(A, n, m)
    less = countKeysLess(equal, m)
    return rearrange(A, less, n, m)
    
if __name__ == '__main__':
    A = [4,1,5,0,77,1,6,5,1,5,3,3,2,4,5,3,2,5,3,3,9]
    res = improveCountingSort(A)
    print(res)
    
