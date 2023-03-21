class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        result = 0
        arr.append(float("-inf"))
        stack = []
        for i , num in enumerate(arr):
            while stack and arr[stack[-1]] > num:
                curr = stack.pop()
                right = i
                left = stack[-1] if stack else -1
                sub = (curr-left)*(right-curr)
                result += sub*arr[curr]
            stack.append(i)
        mod = 1000000007
        return result%mod
    