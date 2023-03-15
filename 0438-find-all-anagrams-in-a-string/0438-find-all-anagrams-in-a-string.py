class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        Pcount, Scount = {}, {}
        for i in range (len(p)):
            Pcount[p[i]] = 1 + Pcount.get(p[i], 0)
            Scount[s[i]] = 1 + Scount.get(s[i], 0)
        result = [0] if Pcount == Scount else []
        left = 0
        right = len(p)
        while right < len(s):
            Scount[s[right]] = 1 + Scount.get(s[right], 0)
            Scount[s[left]] -= 1
            
            if Scount[s[left]] == 0:
                del Scount[s[left]]
            left += 1
            if Scount == Pcount:
                result.append(left)
            right += 1
        return result