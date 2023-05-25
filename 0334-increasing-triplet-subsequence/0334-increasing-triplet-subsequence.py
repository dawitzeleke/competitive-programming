class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        minsofar = float("inf")
        second = float("inf")
        
        for num in nums:
            if num > second:
                return True
            if num > minsofar:
                second = min(second, num)
            minsofar = min(minsofar, num)
        return False