"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None

        curr = head

        while curr:
            next_node = curr.next

            new_node = Node(curr.val, next_node)

            curr.next = new_node

            curr = new_node.next

        curr = head

        while curr:

            if curr.random:
                curr.next.random = curr.random.next

            curr = curr.next.next

        curr = head

        new_head = head.next

        new_curr = new_head


        while curr:
            curr.next = new_curr.next
            curr = curr.next
            if curr:
                new_curr.next = curr.next
                new_curr = new_curr.next

        return new_head