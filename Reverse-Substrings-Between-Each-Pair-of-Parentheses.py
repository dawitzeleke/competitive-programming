class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if (s[i] == '('):
                stack.append(i)
            elif (s[i] == ')'):
                temp = s[stack[-1]:i + 1]
                s = s[:stack[-1]] + temp[::-1] + s[i + 1:]
                del stack[-1]
 
        result = ""
        for i in range(len(s)):
            if (s[i] != ')' and s[i] != '('):
                result += (s[i])
        return result
