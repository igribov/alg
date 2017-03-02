def insertationSort(A, n):
    for i in range(1, n):
        key = A[i] # вытаскиваем текущее значение
        j = i - 1 # предыдущая позиция
        while j >= 0 :# передвигаем пока предыдущее больше
            
            if A[j] > key:
                A[j+1] = A[j]
                A[j] = key
            j-=1
        
    return A

if __name__ == '__main__':
    A = [22,8,5,2,100,15,13,16,18,14,11,10,6,5,8,3,1,22,43,4]
    A = [11,10,9,8,7,6,5,4,3,2,1,12,13,14,15,16,17]
    
    res = insertationSort(A, len(A));
    print(A)
