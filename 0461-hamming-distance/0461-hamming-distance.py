class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        counter = 0
        while x and y:
            if x & 1 != y & 1:
                counter += 1
            x >>= 1
            y >>= 1
        while x:
            if x & 1 != y & 1:
                counter += 1
            x >>= 1
        while y:
            if x & 1 != y & 1:
                counter += 1
            y >>= 1
        return counter 