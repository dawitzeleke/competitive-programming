class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(y, p):
            if p == 0:
                return 1
            if p % 2 == 0:
                return power( y * y, p/2)
            return y * power( y * y, (p-1)/2)
        if n >= 0:
            return power(x, n)
        elif n < 0: 
            return power(1/x, -(n))