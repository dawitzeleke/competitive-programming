import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        max_num = 3**19
        return n>0 and max_num%n==0
