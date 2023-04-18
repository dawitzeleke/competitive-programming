# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        len_cycle = 0
        slow = head
        fast = head
        
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                temp = slow
                temp = temp.next
                len_cycle += 1
                while fast != temp:
                    len_cycle += 1
                    temp = temp.next
                break
        
             
        if len_cycle == 0:
            return None
        first = head
        second = head
        
        while len_cycle > 0:
            second = second.next
            len_cycle -= 1
        
        while first != second:
            first = first.next
            second = second.next
        
        return second
       
        
