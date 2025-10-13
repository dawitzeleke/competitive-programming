class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        max_len = float("-inf")
        char_count = defaultdict(int)

        for right in range(len(s)):

            char_count[s[right]] += 1


            while char_count[s[right]] > 1:
                char_count[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len if max_len != float("-inf") else 0

            