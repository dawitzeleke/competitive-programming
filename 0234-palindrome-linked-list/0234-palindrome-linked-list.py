# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = []
        
        while head:
            temp.append(head.val) 
            head = head.next
            
            
        left = 0
        right = len(temp) - 1
        while right > left:
            if temp[left] != temp[right]:
                return False
            else:
                left += 1
                right -= 1
        return True