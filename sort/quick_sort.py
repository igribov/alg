def partition(A, p, r, log=0):
    if(log):print(A, p, r)
    q = p
    P = A[r]
    if(log) : print('Опорный элемент %d' % P)
    for u in range(p, r):
        if(log) : print('=' * 10)
        if(log) : print('Берем ', A[u])
        if(log) : print('Сравниваем A[%d]=%d и %d' % (u, A[u] , P))
        if A[u] >= A[r]:
            if(log) : print('%d больше или равно %d' % (A[u] , P))
            if(log) : print('не сдвигаем q %d->%d' % (q, q))
        else:
            msg = '%d меньше %d -> меняем местами A[q]=%d и A[u]=%d'
            if(log) : print( msg % (A[u], P, A[q], A[u]) )
            if(log) : print('сдвигаем q %d->%d' % (q, q + 1))
            let = A[q]
            A[q] = A[u]
            A[u] = let
            q+=1
    if(log) : print('Меняем местами A[q]=%d и Опрорный %d' % (A[u], A[r]))
    let = A[q]
    A[q] = A[r]
    A[r] = let
    if(log) : print(q)
    if(log) : print(A)
    return q

def quickSort(A, p, r):
    if p >= r:
        return
    q = partition(A, p, r)
    quickSort(A, p, q-1)
    quickSort(A, q+1, r)
    

if __name__ == '__main__':
    
    A = [9,7,5,11,12,2,14,3,10,6]
    quickSort(A,0,len(A)-1)

    print(A)
    '''
    q2 = partition(A,0,q-1)
    print(q2, A)

    q3 = partition(A,q,len(A)-1)
    print(q3, A)

    q4 = partition(A,0,q2-1)
    print(q4, A)

    q5 = partition(A,q3,len(A)-1)
    print(q5, A)

    q6 = partition(A,0,q4-1)
    print(q6, A)

    q7 = partition(A,q5,len(A)-1)
    print(q7, A)
    '''



