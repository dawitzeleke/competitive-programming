"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        curr = head  

        while curr:

            if curr.child:

                curr_child = curr.child
                next_node = curr.next

                temp = curr_child

                while temp.next:
                    temp = temp.next
                curr_end = temp
                curr.next = curr_child
                curr_child.prev = curr
                curr_end.next = next_node
                if next_node:
                    next_node.prev = curr_end

            curr.child = None
            curr = curr.next

        return head