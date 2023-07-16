class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        memo = {}
        
        for num in arr:
            temp = num - difference
            
            if temp in memo:
                memo[num] = 1 + memo[temp]
            else:
                memo[num] = 1
                
        return max(memo.values())