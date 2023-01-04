
class Solution:
    def isPalindrome(self, x):
        rev=0
        num= x
        while x>0:
            div= x%10
            rev = rev*10 + div
            x= x//10  
        
        if rev == num:
            return True
        else:
            return False

