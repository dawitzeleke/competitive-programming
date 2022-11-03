import operator

class Solution:
    def evalRPN(self, tokens):
        if tokens == []:
            return -1
        
        stack = [] 
        
        ops = ["+", "-", "*", "/"]
        ops_lookup = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
        
        for token in tokens:            
            if token not in ops:
                stack.append(int(token))
            else:
                val1 = stack.pop(-1)
                val2 = stack.pop(-1)
                result = ops_lookup[token](val2, val1)
                stack.append(int(result))
            
        return stack.pop()
