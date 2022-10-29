def insertionSort1(n, arr):
    num= arr[-1]
    i= n-1
    while i>0 and arr[i-1]>num:
        arr[i]=arr[i-1]
        print(*arr)
        i-=1
    arr[i]=num
    print(*arr)
