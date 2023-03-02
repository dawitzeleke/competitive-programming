class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1
        else:
            return self.fib(n-2) + self.fib(n-1)  