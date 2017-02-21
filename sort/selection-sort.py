def selectionSortWithLog(A, n):
    # Каждую итерацию укорачивается подмассив
    for i in range(0, n):
        print(' '*4*i,A[i:n],end='')
        smallest = i
        # Ищем наименьший элемент в подмассиве
        for j in range(i+1, n):
            if A[j] < A[smallest]: smallest = j
        print('smallest A[%d]= %d' % (smallest, A[smallest]),end='\n')
        # Меняем его местами с первым элементом подмассива
        c = A[i]
        A[i] = A[smallest]
        A[smallest] = c
    return A

def selectionSort(A, n):
    for i in range(0, n):
        smallest = i
        for j in range(i+1, n):
            if A[j] < A[smallest]: smallest = j
        c = A[i]
        A[i] = A[smallest]
        A[smallest] = c
    return A

if __name__ == '__main__':
    A = [ 43,34,42,12,54,14,64,31,73,51,18,10,92,53,84,35,27,56,36,22]
  
    print(selectionSort(A, len(A)))

    
