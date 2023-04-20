class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        if len(s) > 12:
            return res
        
        def helper(index, dots, curr):
            if dots == 4 and index == len(s):
                
                res.append(curr[:-1])
                return 
            
            if dots > 4:
                return
            for j in range(index , min(index + 3, len(s))):
                if int(s[index: j + 1]) < 256 and (index == j or s[index] != "0"):
                    helper(j + 1, dots + 1, curr + s[index: j + 1] + ".")
                    
        helper(0, 0, "")
        return res