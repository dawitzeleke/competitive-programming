class Solution(object):
    def reverseParentheses(self, s):
        stack = []

        for char in s:
            if char == "(":
                stack.append(char)
            elif char == ")":
                sub_s = []
                while stack[-1] != "(":
                    sub_s.append(stack.pop())
                stack.pop()
                stack.extend(sub_s)
            else: 
                stack.append(char)
        
        return "".join(stack)
