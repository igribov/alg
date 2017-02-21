from math import inf as INF, ceil
import copy

def merge(A, p, q, r):
    #A = copy.copy(A1)
    n1 = q - p
    n2 = r - q
    B = A[p : q] + [INF]
    C = A[q : r +  1] + [INF]
    #print(B, C)
    i = j = 0
    for k in range(p, r-1):
        #print(B[i], C[j])
        if B[i] <= C[j] :
            A[k] = B[i]
            i+=1
        else:
            A[k] = C[j]
            j+=1
    print(A)

def mergeSort(A,p,r):
    #print(p, r)
    if p < (r-1) :
        q = ceil((p + r) / 2)
        #print(A[p:q],p,q)
        #print(A[q+1:r], q+1,r)
        mergeSort(A,p,q)
        print(A)
        mergeSort(A,q+1,r)
        merge(A,p,q,r)
    else:
        return
    

A = [1,4,7,99, 6, 8,88]
#A = [9,8,7,6,5,4,3,2,1]
middle  = 4
print(A, 0, middle, len(A))
#middle = 7
merge(A, 0, middle, len(A))

#mergeSort(A, 0, len(A)-1)
#print(A)

