class Solution(object):
    def largestNumber(self, nums):
        n= len(nums)
        largest_num=""

        for i in range(n):
            for j in range (i+1, n):
                if nums[i]!=0 or nums[j]!=0:
                    sum1= str(nums[i]) + str(nums[j])
                    sum2= str(nums[j]) + str(nums[i])
                    if int(sum1)< int(sum2):
                        nums[i],nums[j]= nums[j],nums[i]
                    else:
                        continue
        for k in range(n):
            largest_num+= str(nums[k])
        
        return str(int(largest_num))
