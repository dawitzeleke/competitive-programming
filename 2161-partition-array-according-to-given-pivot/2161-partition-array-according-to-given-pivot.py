class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        pivots = []
        greater = []

        for num in nums:
            if num == pivot:
                pivots.append(num)

            elif num > pivot:
                greater.append(num)

            else:
                less.append(num)

        return less + pivots + greater