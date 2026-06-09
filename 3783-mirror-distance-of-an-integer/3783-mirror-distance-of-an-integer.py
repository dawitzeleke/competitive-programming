class Solution:
    def mirrorDistance(self, n: int) -> int:
        reverse = str(n)[::-1]

        return abs(n - int(reverse))