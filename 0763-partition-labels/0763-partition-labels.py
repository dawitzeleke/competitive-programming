class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {i:num for num,i in enumerate(s)}
        
        left = 0 
        right = -1
        current = ""
        res = []
        while(left< len(s)):    
            char = s[left]
            right = max(d[char] , right)
            current += char
            if left == right:
                res.append(len(current))
                current = ""
            left +=1
        
        return res