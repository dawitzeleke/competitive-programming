class Solution: 
    def select(self, arr, i):
        n= len(arr)
        for i in range(n-1):
            selected= arr[i]
            for j in range(i+1, n):
                if selected>arr[j]:
                    selected= min(selected, arr[j])
                else:
                    continue
        return selected
    
    def selectionSort(self, arr,n):
        for i in range (n-1):
            minn= i
            for j in range(i+1,n):
                if arr[j]<arr[minn]:
                    minn= j
                else:
                    continue
            if minn!= i:
                arr[i], arr[minn]= arr[minn], arr[i]
        return arr
