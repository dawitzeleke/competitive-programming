# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        queue = []
        lis = []
        while head:
            if head.val >= x:
                queue.append(head.val)
            else:
                lis.append(head.val)
            head = head.next
        lis += queue
        d = n = ListNode()
        for i in lis:
            n.next = ListNode(i)
            n = n.next
        return d.next