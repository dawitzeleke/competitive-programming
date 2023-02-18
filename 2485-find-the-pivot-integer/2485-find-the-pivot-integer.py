class Solution:
    def pivotInteger(self, n: int) -> int:
        s = 0
        for i in range (1,n+1):
            s += i
        r_s = s
        l_s = 0
        for i in range(1,n+1):
            l_s += i
            if l_s == r_s:
                return i
            else:
                r_s  -= i
        return -1