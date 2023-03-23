class Solution:
    def quicksort(self, arr, start, end):

        if end  - start <= 0:
            return
        pivot = arr[start]
        write = start + 1
        for read in range(start + 1, end + 1):
            if arr[read] <= arr[start]:
                arr[read], arr[write] = arr[write], arr[read]
                write += 1
        arr[start], arr[write - 1] = arr[write - 1], arr[start]
        if len(arr) - self.k < write - 1:
            self.quicksort(arr, start, write - 2)
        else:
            self.quicksort(arr, write , end)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.k = k
        self.quicksort(nums, 0, len(nums) - 1)
        return nums[len(nums) - k]