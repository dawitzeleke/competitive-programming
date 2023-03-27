class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        self.res = 0
        dif = []
        for i in range(len(nums1)):
            dif.append(nums1[i] - nums2[i])
            
        def binary_search(l, r, arr, target):
            counter = 0
            while l <= r:
                mid = (l + r)//2
                if arr[mid] <= target:
                    counter += 1
                    l = mid + 1
                   
                elif arr[mid] > target:
                    r = mid - 1
            return l
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
            for i in range(len(right_half)):
                temp = binary_search(0, len(left_half) - 1, left_half, right_half[i] + diff)
                self.res += temp
            while l1 < len(left_half) and l2 < len(right_half):
                if left_half[l1] > right_half[l2]:
                    result.append(right_half[l2]) 
                    l2 += 1
                elif left_half[l1] <= right_half[l2]:
                    result.append(left_half[l1])
                    l1 += 1
            while l1 < len(left_half):
                result.append(left_half[l1])
                l1 += 1
            while  l2 < len(right_half):
                result.append(right_half[l2])
                l2 += 1
            return result
                
        mergeSort(0, len(dif) - 1, dif)       
        return self.res
    