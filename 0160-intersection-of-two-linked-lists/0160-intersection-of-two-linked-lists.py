# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def get_length(node):
            if not node:
                return None
            
            temp = node
            length = 0
            while temp:
                length += 1
                temp = temp.next
            return length

        len_a = get_length(headA)
        len_b = get_length(headB)

        temp_a = headA
        temp_b = headB

        while len_a > len_b:
            len_a -= 1
            temp_a = temp_a.next

        while len_b > len_a:
            len_b -= 1
            temp_b = temp_b.next

        while temp_a != temp_b:
            temp_a = temp_a.next
            temp_b = temp_b.next

        return temp_a
