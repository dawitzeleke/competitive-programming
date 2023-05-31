class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n
       
        fib1 = 0
        fib2 = 1
        fib3 = 1
        
        for i in range(3, n + 1):
            temp = fib1 + fib2 + fib3
            fib1 = fib2
            fib2 = fib3
            fib3 = temp
            
        return fib3