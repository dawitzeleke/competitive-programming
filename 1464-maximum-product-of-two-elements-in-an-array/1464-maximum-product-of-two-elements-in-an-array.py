class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heap = []
        
        for num in nums:
            heappush(heap, - num)
            
        return (( - heappop(heap)) - 1) * (( - heappop(heap)) - 1)