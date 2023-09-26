class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        
        @cache
        def dp(index , factor):
            if index == len(satisfaction):
                return 0
            
            takeIt =  satisfaction[index]*factor + dp(index + 1, factor + 1)
            leaveIt  = dp(index + 1, factor)
            
            return max(takeIt, leaveIt)
        
        return dp(0,1)
            
                