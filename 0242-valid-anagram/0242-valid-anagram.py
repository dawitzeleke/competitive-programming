class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        fre1 = {}
        fre2 ={}
        if len(s) != len(t):
            return False
        for i in s:
            if i in fre1:
                fre1[i] +=1
            else:
                fre1[i] = 1
        for i in t:
            if i in fre2:
                fre2[i] +=1
            else:
                fre2[i] = 1
        for c in t:
            if c in fre1 and fre2[c] == fre1[c]:
                continue
            else:
                return False
                
        return True
            