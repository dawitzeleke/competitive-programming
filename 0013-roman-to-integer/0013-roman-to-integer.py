class Solution:
    def romanToInt(self, s: str) -> int:
        r={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        tot=0
        for i in range(len(s)-1):
            if r[s[i]] < r[s[i+1]]:
                tot-=r[s[i]]
            else:
                tot+=r[s[i]]
        tot+=r[s[-1]]
        return tot