class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        answer = []
        def backtracking(index, curr_subset):
            if index == length:
                answer.append(curr_subset[:])
                return

            curr_subset.append(nums[index])
            backtracking(index + 1, curr_subset)
            curr_subset.pop()
            backtracking(index + 1, curr_subset)

        backtracking(0, [])

        return answer
