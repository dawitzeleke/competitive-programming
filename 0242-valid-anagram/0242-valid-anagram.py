class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        t_count = defaultdict(int)
        s_count = defaultdict(int)
        if len(s) != len(t):
            return False

        for char in t:
            t_count[char] += 1

        for char in s:
            s_count[char] += 1


        for char, count in t_count.items():
            if s_count[char] != count:
                return False

        return True 