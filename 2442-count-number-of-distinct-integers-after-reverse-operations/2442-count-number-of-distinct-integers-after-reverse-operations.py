from collections import Counter
class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        res = set()
        
        for num in nums:
            res.add(num)
            res.add(int(str(num)[::-1]))
    
        
        return len(res)
        