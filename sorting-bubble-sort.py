def countSwaps(a):
    numSwaps= 0
    n= len(a)
    for i in range(n):
        j= 0
        while j< n-1:
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                numSwaps+=1
            j+=1
    print("Array is sorted in" ,numSwaps, "swaps.")  
    print("First Element:", a[0])          
    print("Last Element:" , a[-1])
