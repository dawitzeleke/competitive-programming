class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in  {"+", "-", "*", "/"}:
                stack.append(token)
            else:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                temp = 0
                if token == "+":
                    temp = num2 + num1
                elif token == "-":
                    temp = num2 - num1
                elif token == "*":
                    temp = num2 * num1
                elif token == "/":
                    temp = int(num2 / num1)
                stack.append(str(temp))

        return int(stack[0])