class Solution(object):
    def isValid(self, s):
        dictionary = { "(": ")" , "[":"]" , "{":"}"}
        stack = []
        for p in s:
            if p in dictionary.keys():
                stack.append(p)
            else: 
                if not len(stack):
                    return False 
                else:
                    x= stack.pop()
                    if p != dictionary[x]:
                        return False
        return not len(stack)
