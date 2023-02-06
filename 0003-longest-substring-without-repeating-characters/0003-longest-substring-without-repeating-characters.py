class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        max_len = 0
        left = 0
        right = 0

        while right < len(s):
            if s[right] not in substring:
                substring.add(s[right])
                right += 1
                max_len = max(max_len, right - left)
            else:
                substring.remove(s[left])
                left += 1
        return max_len