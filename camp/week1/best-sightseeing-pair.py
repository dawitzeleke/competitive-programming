class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        i = 0
        res = -float("inf")
        
        for j in range(1, len(values)):
            res = max(values[i] + values[j] + i - j, res)
            if values[i]+ i < values[j]  + j:
                i = j
                
        return res