class Solution:
    def findComplement(self, num: int) -> int:
        answer = 0 
        digit = 0
        
        while num :
            if num & 1 != 1:
                answer += 2**digit
            
            num >>= 1
            digit += 1
            
        return answer
        