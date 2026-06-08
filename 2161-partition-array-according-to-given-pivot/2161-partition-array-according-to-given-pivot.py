class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        i = 0
        j = len(nums) - 1

        i2 = 0
        j2 = len(nums) - 1
        answer = [0] * len(nums)


        while j >= 0:
            if nums[j] > pivot:
                answer[j2] = nums[j]
                j2 -= 1
            if nums[i] < pivot:
                answer[i2] = nums[i]
                i2 += 1
            i += 1
            j -= 1
        while i2 <= j2:
            answer[i2] = pivot
            answer[j2] = pivot
            i2 += 1
            j2 -= 1

        return answer


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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