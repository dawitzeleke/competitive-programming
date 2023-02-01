from math import log
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<= 0:
            return False
        res = (log(n)) / (log(4))
        return res.is_integer()
