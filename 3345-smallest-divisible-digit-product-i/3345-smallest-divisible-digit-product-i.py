class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        

        for num in range(n, 100 + 1):
            product = 1
            temp = num
            while temp > 0:
                product *= temp % 10
                temp //= 10

            if product % t == 0:
                return num

        