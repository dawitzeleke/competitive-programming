class Solution:
    def heapify(self,arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left] > arr[i]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
            
        if largest != i:
            arr[largest], arr[i] = arr[i], arr[largest]
            self.heapify(arr, n, largest)
       
    

    def buildHeap(self,arr,n):
        start = (n // 2) - 1
        
        for i in range(start, -1, -1):
            self.heapify(arr, n, i)
   
    
        
    def HeapSort(self, arr, n):
        self.buildHeap(arr, n)
        
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
          
            self.heapify(arr, i, 0)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.HeapSort(nums, len(nums))
    
        return nums[len(nums) - k]
        