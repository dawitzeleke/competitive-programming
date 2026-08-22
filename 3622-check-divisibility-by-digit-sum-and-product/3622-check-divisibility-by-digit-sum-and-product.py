class Solution:
    def checkDivisibility(self, n: int) -> bool:
        
        digit_sum = 0
        digit_product = 1
        n_temp = n

        while n_temp > 0:
            temp = n_temp % 10

            digit_sum = digit_sum + temp
            digit_product = digit_product * temp

            n_temp //= 10

        x = (digit_sum + digit_product)
        return n % x == 0