def binarySearch(A, i, j, x):
    while True:
        if i > j:
            return -1
        m = (i + j)// 2;
        if x < A[m]:
            j = m - 1
        elif x > A[m]:
            i = m + 1
        else :
            return m

def binarySearchReqursive(A, i, j, x):
    if i > j:
        return -1
    m = (i + j)// 2;
    if x < A[m]:
        j = m - 1
    elif x > A[m]:
        i = m + 1
    else :
        return m
    return binarySearchReqursive(A, i, j, x)

x = 23
A = list(range(1, 122, 2))

f = binarySearch(A, 0, len(A)-1, x)
print(A)
print('x==> index %s' % f if f!=-1 else 'NOT FOUND')

f = binarySearchReqursive(A, 0, len(A)-1, x)
print('x==> index %s' % f if f!=-1 else 'NOT FOUND')
