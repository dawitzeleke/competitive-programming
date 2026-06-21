class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        n = len(nums)

        prefix = [0] * (n + 1)
        valid = 0
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        for i in range(n):

            for j in range(i, n):

                current_sum = abs(prefix[j + 1] - prefix[i])
                if (int(str(current_sum)[0]) == x) and (int(str(current_sum)[-1]) == x):
                    valid += 1

        return valid
