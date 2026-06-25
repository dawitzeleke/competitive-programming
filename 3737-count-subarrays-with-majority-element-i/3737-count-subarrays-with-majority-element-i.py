class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            target_count = 0
            for j in range(i, n):
                if nums[j] == target:
                    target_count += 1

                length = j - i + 1
                if 2 * target_count > length:
                    count += 1
        return count