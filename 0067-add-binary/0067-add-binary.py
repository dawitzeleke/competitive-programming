class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_ptr = len(a) - 1
        b_ptr = len(b) - 1

        answer = ""

        carry = 0

        while a_ptr >= 0 or b_ptr >= 0:
            curr_sum = carry
            
            if a_ptr >= 0:
                curr_sum += int(a[a_ptr])
                a_ptr -= 1
            if b_ptr >= 0:
                curr_sum += int(b[b_ptr])
                b_ptr -= 1

            answer = str(curr_sum % 2) + answer
            carry = curr_sum // 2
        
        if carry:
            answer = "1" + answer

        return answer
        
