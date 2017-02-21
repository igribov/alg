import random, time

def merge(A, B):
    Res = []
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            Res.append(A[i])
            i += 1
        else:
            Res.append(B[j])
            j += 1
    Res += A[i:] + B[j:]
    return Res

def MergeSort(A):
    if len(A) <= 1:
        return A
    else:
        p = len(A) // 2
        A1 = MergeSort(A[:p])
        A2 = MergeSort(A[p:])
    return merge(A1, A2)
    

A = [random.randint(1,500) for i in range(200000)]

start = time.time()
A1 = MergeSort(A)
end = time.time()
print(end - start)

A = [random.randint(1,500) for i in range(200000)]

start = time.time()
A.sort()
end = time.time()
print(end - start)

#A2 = A.sort()
#print(A1, A)
