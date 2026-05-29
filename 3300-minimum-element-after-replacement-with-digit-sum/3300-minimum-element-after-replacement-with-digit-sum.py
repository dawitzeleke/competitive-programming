class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_element = float("inf")

        for num in nums:
            current_sum = 0
            for char in str(num):
                current_sum += int(char)

            min_element = min(current_sum, min_element)

        return min_element