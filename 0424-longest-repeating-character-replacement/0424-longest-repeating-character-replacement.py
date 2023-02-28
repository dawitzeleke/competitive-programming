class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        helper_dictinary = {}
        max_length = 0
        left =  0
        right = 0 
        
        while right < len(s):
            if s[right] not in helper_dictinary:
                helper_dictinary[s[right]] = 1
            else:
                helper_dictinary[s[right]] += 1
            while (right - left + 1) - max(helper_dictinary.values()) > k:
                helper_dictinary[s[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
            right += 1
            
        return max_length