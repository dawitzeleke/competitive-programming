class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = []
        
        def helper(candidate, candidate_sum, index):
            if candidate_sum == target:
                answer.append(candidate[:])
                return
            if index == len(nums) or  candidate_sum > target:
                return 
            candidate.append(nums[index])
            helper(candidate, candidate_sum + nums[index], index)
            candidate.pop()
            helper(candidate, candidate_sum, index + 1)

        helper([], 0, 0)
        return answer