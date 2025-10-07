# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()
        # find peak

        left = 1
        right = length - 2
        peak = 0

        while left <= right:
            mid = (left + right) // 2
            low, midd, high = mountainArr.get(mid - 1), mountainArr.get(mid), mountainArr.get(mid + 1)
            if low < midd > high:
                peak = mid
                break 
            elif high > midd:
                left = mid + 1

            else:
                right = mid - 1
        highh = peak
        loww = 0
        while loww <= highh:
            mid = (highh + loww) // 2

            midValue = mountainArr.get(mid)

            if midValue > target:
                highh = mid - 1
            elif midValue < target:
                loww = mid + 1
            else:
                return mid
            
        highleft = length - 1
        lowleft = peak
        while lowleft <= highleft:
            mid = (highleft + lowleft) // 2

            midValue = mountainArr.get(mid)

            if midValue < target:
                highleft = mid - 1
            elif midValue > target:
                lowleft = mid + 1
            else:
                return mid
            
        return -1