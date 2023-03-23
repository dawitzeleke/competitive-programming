class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        left = 0
        right = int(sqrt(c))
        while right >= left:
            if right**2 + left**2 == c:
                return True
            elif right**2 + left**2 > c:
                right -= 1
            else:
                left += 1
                
        return False