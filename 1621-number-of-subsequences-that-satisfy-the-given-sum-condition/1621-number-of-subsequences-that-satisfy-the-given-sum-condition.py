class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        answer = 0 
        length = len(nums)

        MOD = (10 ** 9) + 7

        left = 0
        right = length - 1

        while left <= right:
            if nums[left] + nums[right] <= target:
                answer += pow(2, right - left, MOD)
                answer = answer % MOD
                left += 1

            else:
                right -= 1

        return answer

