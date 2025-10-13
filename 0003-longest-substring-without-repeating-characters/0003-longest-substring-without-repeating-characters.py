class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charcount = {}
        maxlen = 0
        left = 0

        for right in range(len(s)):

            if s[right] not in charcount:
                charcount[s[right]] = 1
            else:
                charcount[s[right]] += 1

            while charcount[s[right]] > 1:
                charcount[s[left]] -= 1
                left += 1
            maxlen = max(maxlen, right - left + 1)

        return maxlen
