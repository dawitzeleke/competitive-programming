class Solution:
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)
        i = len(nums) - k
        while i > 0:
            heappop(nums)
            i -= 1 
        return heappop(nums)