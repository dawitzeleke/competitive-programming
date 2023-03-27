class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        helper_dictionary = {}
        nums = [(nums[i],i) for i in range(len(nums))]
        
        for num in nums:
            helper_dictionary[num] = 0
        def mergeSort(left, right, arr):
            if left == right:
                return [arr[left]]
            mid = left + (right - left) // 2
            left_half = mergeSort(left, mid, arr)
            right_half = mergeSort(mid + 1, right, arr)

            return merge(left_half, right_half)
        def merge(left_half, right_half):
            result = []
            l1 = 0
            l2 = 0
            count = 0
            
            while l1 < len(left_half) and l2 < len(right_half):
                if left_half[l1][0] > right_half[l2][0]:
                    result.append(right_half[l2])
                    l2 += 1
                    count += 1
                elif left_half[l1][0] <= right_half[l2][0]:
                    result.append(left_half[l1])
                    index = left_half[l1][1]
                    answer[index] += count
                    l1 += 1
                    
            while l1 < len(left_half):
                result.append(left_half[l1])
                index = left_half[l1][1]
                answer[index] += count
                l1 += 1
            while  l2 < len(right_half):
                result.append(right_half[l2])
                l2 += 1
            return result
        mergeSort(0,len(nums)-1,nums)
        return answer