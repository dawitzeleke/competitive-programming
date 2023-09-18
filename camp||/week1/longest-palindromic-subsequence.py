class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}
        
        left = 0
        right = len(s) - 1
        
        def longestpal(l, r):
            
            if (l, r) in memo:
                return memo[(l, r)]
            
            if l > r:
                return 0
            if l == r:
                return 1
            maxlen = 0
            if s[l] == s[r]:
                maxlen = 2 + longestpal(l + 1, r - 1)
                
            else:
                maxlen = max(longestpal(l, r - 1), longestpal(l + 1, r))
                
            memo[(l, r)] = maxlen
            
            return memo[(l,r)]
        
        
        return longestpal(left, right)