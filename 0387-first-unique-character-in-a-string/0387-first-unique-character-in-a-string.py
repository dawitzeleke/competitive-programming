class Solution:
    def firstUniqChar(self, s: str) -> int:
        """

        counter = {
            "a" : 2,
            "b" : 2
        }

        aabb
         |
         |

         leetcode
         |
        """

        counter = defaultdict(int)

        for char in s:
            counter[char] += 1

        for i in range(len(s)):
            curr_char = s[i]
            if counter[curr_char] == 1:
                return i

        return -1