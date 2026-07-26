class Solution:
    def maximumProduct(self, A: List[int]) -> int:
        a = b = c = -1001
        x = y = 1001

        for n in A:
            pa, pb, px = a, b, x
            
            a = max(a, n)
            b = max(b, min(pa, n))
            c = max(c, min(pb, n))
            
            x = min(x, n)
            y = min(y, max(px, n))

        return max(a * b * c, a * x * y)