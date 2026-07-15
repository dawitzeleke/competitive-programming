import math

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd = 0
        sumEven = 0

        even = 2
        odd = 1

        for _ in range(n):
            sumEven += even
            sumOdd += odd
            even += 2
            odd += 2

        

        return math.gcd(sumOdd, sumEven)

