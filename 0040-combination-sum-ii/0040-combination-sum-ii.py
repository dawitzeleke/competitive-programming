class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        candidate = []
        visited = set()
        
        _sum = sum( nums )
        if _sum < target:
            return []

        nums.sort()
        def helper(candidate_sum, index):
            if candidate_sum == target :
                curr_combination = tuple( candidate )
                visited.add( curr_combination )
                return
            
            if index == len(nums):
                return
            
            prev = nums[index]
            for i in range( index, len(nums) ):
                if i > index and nums[i] == prev:
                    continue
                if candidate_sum + nums[i] > target:
                    break
                candidate.append(nums[i])
                helper( candidate_sum + nums[i], i + 1 )
                candidate.pop()
                prev = nums[i]
                

        helper(0, 0)
        return visited