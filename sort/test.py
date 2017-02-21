from quick_sort import quickSort
from random import randint
import time, copy

A = [ randint(1,100) for i in range(1, 10000) ]
A2 = copy.copy(A)

start = time.time()
quickSort(A,0,len(A)-1)
end = time.time()

print(end - start)

start = time.time()
A2.sort()
end = time.time()

print(end - start)
