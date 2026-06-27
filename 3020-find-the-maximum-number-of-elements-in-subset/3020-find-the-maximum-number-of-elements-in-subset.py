class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        from collections import Counter

        freq = Counter(nums)
        ans = 1

        if 1 in freq:
            cnt = freq[1]

            ans = max(ans, cnt if cnt % 2 else cnt - 1)

        for start in freq:
            if start == 1:
                continue

            cur = start
            length = 0

            while cur in freq:
                if freq[cur] >= 2:
                    length += 2

                    cur *= cur
                else:
                    length += 1
                    break

            if length % 2 == 0:
                length -= 1

            ans = max(ans, length)

        return ans