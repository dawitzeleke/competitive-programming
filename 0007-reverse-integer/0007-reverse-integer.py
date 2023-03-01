class Solution:
    def reverse(self, x: int) -> int:
        result = 0 
        if x < 0:
            sign = -1
            x = -(x)
        else:
            sign = 1
        
        while x != 0:
            result = result * 10 + x%10
            x = x // 10
        return 0 if result > 2**31 - 1 else result* sign
            