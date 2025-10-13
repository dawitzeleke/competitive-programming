class Solution:
    def myAtoi(self, s: str) -> int:
        """
        first remove the white space
        loop*

        sign = 1 or -1



        """

        sign = 1
        index = 0
        answer = 0
        while index < len(s) and s[index] == " ":
            index += 1

        if index < len(s) and (s[index] == "+" or s[index] == "-"):
            if s[index] == "-":
                sign = -1
            index += 1
        
        while index < len(s) and "0" <= s[index] <= "9":
            answer = 10 * answer + int(s[index])
            if int(answer) > (2**31 - 1):
                return 2**31 - 1 if sign == 1 else -2**31
            index += 1

        return (int(answer)) * sign

        