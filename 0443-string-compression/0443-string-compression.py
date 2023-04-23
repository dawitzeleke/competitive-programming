from collections import Counter
class Solution:
    
    def compress(self, chars: List[str]) -> int:
       
        right = 0
        temp = chars[right]
        length = 0
        s = ""
        while right < len(chars):
            if chars[right] == temp :
                length += 1
                right += 1
            else:
                s += temp
                if length > 1:
                    s += str(length)
                length = 0
                temp = chars[right]
                    
        s += temp
        if length > 1:
            s += str(length)
        for i in range(len(s)):
            chars[i] = s[i]
            
        return len(s)
        