class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def recursivefun(left, right, s):
            if left >= right:
                return s[left]
            else:
                s[left], s[right] = s[right], s[left]
                return recursivefun(left+1, right-1, s)
        return recursivefun(0, len(s)-1, s)