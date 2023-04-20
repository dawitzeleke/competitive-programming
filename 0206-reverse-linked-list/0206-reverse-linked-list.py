# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.res = None
        def helper(node):
            if not node.next:
                self.res = node
                return node 
            p = helper(node.next)
            p.next = node
            node.next = None

            return node
        if not head:
            return None
        helper(head)
        return self.res
