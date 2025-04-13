class Solution:
    def countGoodNumbers(self, n: int) -> int:
        evenNumber = 5
        primeNumber = 4
        mod = (10**9) + 7
        evenPower = 0
        primePower = 0
        if n % 2 == 0:
            evenPower = n // 2
            primePower = n // 2
        else:
            evenPower = ((n - 1) // 2) + 1
            primePower = (n - 1) // 2

        answer = (pow(evenNumber, evenPower,mod)) * (pow(primeNumber, primePower,mod))
        return answer % mod
