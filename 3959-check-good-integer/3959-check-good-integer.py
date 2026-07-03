class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        squareSum = 0
        digitSum = 0

        while n > 0:
            cur_n = n % 10
            squareSum += (cur_n ** 2)
            digitSum += (cur_n)

            n //= 10
        return squareSum - digitSum >= 50
