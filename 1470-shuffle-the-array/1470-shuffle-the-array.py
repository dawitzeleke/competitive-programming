class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        answer = []

        x = 0 
        y = n 
        x_turn = True

        while y < len(nums):
            if x_turn:
                answer.append(nums[x])
                x_turn = False
                x += 1
            else:
                answer.append(nums[y]) 
                x_turn = True
                y += 1

        return answer
            