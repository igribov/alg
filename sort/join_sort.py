from math import inf as INF, ceil

def merge(A, p, q, r):
    
    B = A[p:q] + [INF]
    C = A[q:r] + [INF]
    
    i = j = 0
    for k in range(p, r):
        if B[i] <= C[j] :            
            A[k] = B[i]
            i+=1
        else:
            A[k] = C[j]
            j+=1

def mergeSort(A, p, r):
    if len(A[p:r]) <= 1:
        return A
    if p < r :
        q = ceil((p + r) / 2)
        mergeSort(A, p, q)
        mergeSort(A, q, r)
        merge(A, p, q, r)
    else:
        return
    

A = [1,7,4,99,6,8,88,3,29,-1,99,-2,102]
#A = [6,7,8,9,10,11, 1,2,3,4,5,5.5]
#middle  = 6

#merge(A, 0, middle, len(A)-1)

mergeSort(A, 0, len(A))
print(A)

