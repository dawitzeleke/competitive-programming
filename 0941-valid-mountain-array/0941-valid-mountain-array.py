class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        left = 0
        right = len(arr) - 1 
        while arr[left] < arr[left + 1] and left + 1 < right:
            left += 1
        while arr[right - 1] > arr[right] and 0 < right - 1:
            right -= 1
        if left == right and right != len(arr) - 1 and left != 0:
            return True
        return False