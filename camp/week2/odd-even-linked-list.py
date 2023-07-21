# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None or head.next.next==None:
            return head
        t1=head
        temp=t2=head.next
        while t2.next and t2.next.next:
            t1.next=t2.next
            t2.next=t2.next.next
            t1=t1.next
            t2=t2.next            
        if t2.next:
            t1.next=t2.next
            t2.next=None
            t1=t1.next
        t1.next=temp
        return head 