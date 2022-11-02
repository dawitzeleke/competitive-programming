class Solution(object):
    def kthLargestNumber(self, nums, k):
        Nums=[int(i) for i in nums]
        sorted_nums= sorted(Nums)
        return str(sorted_nums[len(sorted_nums)-k])
        
