# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ptr = ListNode(-1)
        dummy.next = head
        
        while head and head.next:
            
            if head.val == head.next.val:
                
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                ptr.next = head
                
            else:
                head = head.next
                ptr = ptr.next
                
        return dummy.next