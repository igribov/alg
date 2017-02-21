def insertationSort(A, n):
    for i in range(1, n):
        key = A[i] # вытаскиваем текущее значение
        j = i - 1 # предыдущая позиция        
        while j >= 0 and A[j] > key: # передвигаем пока пред. больше
            A[j+1] = A[j]
            j-=1
        A[j+1] = key
    return A

def insertationSort2(A, n):
    for i in range(0, n):
        key = A[i] # вытаскиваем текущее значение
        j = i - 1 # предыдущая позиция        
        while j > -1 and A[j] > key: # передвигаем пока пред. больше
            A[j+1] = A[j]
            j-=1
        A[j+1] = key
    return A

if __name__ == '__main__':
    A = [22,8,5,2,100,15,13,16,18,14,11,10,6,5,8,3,2,1,22,43,4]
    
    res = insertationSort(A, len(A));
    print(res, len(res), len(A))
