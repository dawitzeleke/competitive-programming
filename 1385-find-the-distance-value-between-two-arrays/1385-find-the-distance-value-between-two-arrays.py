class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2 = sorted(arr2) + [inf]  # sentinel: some b is always >= a - d

        def far(a):  # the first b >= a - d is already past a + d
            return arr2[bisect_left(arr2, a - d)] > a + d

        return sum(map(far, arr1))