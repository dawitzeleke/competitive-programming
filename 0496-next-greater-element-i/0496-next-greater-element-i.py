class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = [nums2[-1]]
        res = [-1]*len(nums2)
        
        for i in range (len(nums2)-2, -1, -1):
            if nums2[i] < stack[-1]:
                res[i] = stack[-1]
                stack.append(nums2[i])
            else:
                stack.pop()
                while stack:
                    if stack[-1] > nums2[i]:
                        res[i] = stack[-1]
                        stack.append(nums2[i])
                        break
                    else:
                        stack.pop()
                    
                else:
                    stack.append(nums2[i])

        
        for i in range (len(nums1)):
            nums1[i] = res[nums2.index(nums1[i])]
        
        return nums1