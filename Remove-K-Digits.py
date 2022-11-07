class Solution(object):
    def removeKdigits(self, num, k):
        stack = ["0"]
        if len(num)==k:
            return "0"
        for i in range(len(num)):
            while stack[-1] > num[i] and k > 0:
                stack.pop()
                k=k-1
            stack.append(num[i])
        while k>0:
            stack.pop()
            k-=1
        while stack[0] == "0" and len(stack)>1:
            stack.pop(0)
        return "".join(stack)
