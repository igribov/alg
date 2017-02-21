def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

A = [13,12,45,66,13,65,34,23,11,1,6,3,67,8,3]
print(A, len(A))
bubbleSort(A)
print(A)

'''
for( i=0; i < size; i++) {            // i - номер прохода
    for( j = size-1; j > i; j-- ) {     // внутренний цикл прохода
      if ( a[j-1] > a[j] ) {
      x=a[j-1]; a[j-1]=a[j]; a[j]=x;
    }
  }'''
