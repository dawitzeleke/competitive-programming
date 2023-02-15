class Solution:
    def isHappy(self, n: int) -> bool:
        if  n == 1:
            return True
        squares = []
        while True:
            n = sum( (int(i))**2 for i in str(n))
           
            if n == 1:
                return True
            if n in squares:
                return False
            else:
                squares.append(n)
    