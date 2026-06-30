class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = {}
        
        numofsub = 0

        left = 0
        right = 0

        while right < len(s):
            if s[right] not in count:
                count[s[right]] = 1
            else:
                count[s[right]] += 1
        
            while len(count) == 3:
                numofsub += len(s) - right
                count[s[left]] -= 1

                if count[s[left]] == 0:
                    del count[s[left]]
                
                left += 1
            right += 1

        return numofsub