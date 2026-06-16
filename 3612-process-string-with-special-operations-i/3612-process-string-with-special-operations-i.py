class Solution:
    def processStr(self, s: str) -> str:
        length = len(s)
        result = ""

        for char in s:
            if char == "*":
                if len(result) > 0:
                    result = result[:len(result) - 1]

            elif char == "#":
                result = result + result
            elif char == "%":
                result = result[::-1]


            else:
                result +=  char

        return result