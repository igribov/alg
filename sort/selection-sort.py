
def selectionSort(A, n):   
    for i in range(0, n):
        smalest = i        
        for j in range(i+1, n):
            if A[j] < A[smalest]: smalest = j
        c = A[i]
        A[i] = A[smalest]
        A[smalest] = c
    return A

if __name__ == '__main__':
    A = [ 4,3,4,2,5,14,6,3,7,5,8,10,9,5,8,3,2,56,36,22]
    res = [2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 14, 22, 36, 56]
    print(selectionSort(A, len(A)))
    assert(res == A)
    
