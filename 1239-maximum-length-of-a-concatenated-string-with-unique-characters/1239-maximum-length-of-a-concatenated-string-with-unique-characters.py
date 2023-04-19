class Solution:
    def helper(self, temp , sub):
        
        if len(temp) == len(set(temp)):
            self.ans = max(self.ans , len(temp))
        
        for i in range(len(sub)):
            self.helper(temp + sub[i], sub[i+1:])
    def maxLength(self, arr: List[str]) -> int:
        self.ans = -float("inf")
        self.helper("", arr)
        
        return self.ans