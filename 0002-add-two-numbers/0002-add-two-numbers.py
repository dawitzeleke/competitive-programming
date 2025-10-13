# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummyNode = ListNode()
        prev = dummyNode
        head1 = l1
        head2 = l2
        carry = 0


        while head1 or head2 or carry:
            curr_sum = carry

            if head1:
                curr_sum += head1.val
                head1 = head1.next
            if head2:
                curr_sum += head2.val
                head2 = head2.next

            carry = curr_sum // 10

            curr_val = curr_sum % 10

            new_node = ListNode(curr_val)

            prev.next = new_node

            prev = prev.next

        return dummyNode.next

        