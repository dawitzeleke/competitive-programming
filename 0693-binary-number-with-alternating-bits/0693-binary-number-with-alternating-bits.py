class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bit = n & 1
        n >>= 1
        while n:
            temp = n & 1
            if temp == bit:
                return False
            else:
                bit = temp
                n >>= 1
        return True
        