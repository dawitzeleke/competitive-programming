class Solution:
    def minSteps(self, n: int) -> int:
        c = 0
        prime = 2
        
        while n > 1:
            while n%prime == 0:
                c += prime
                n /= prime
            if prime == 2:
                prime += 1
            else:
                prime += 2
        return c