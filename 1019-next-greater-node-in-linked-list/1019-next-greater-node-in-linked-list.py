# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        size = 0
        p = head
        while p:
            size += 1
            p = p.next
        result = [0] * size
        stack = []
        q = head
        i = 0
        while q:
            currVal = q.val
            while stack and stack[len(stack) - 1][1] < currVal:
                index = stack[-1][0]
                result[index] = currVal
                stack.pop()
            stack.append([i, q.val])
            q = q.next
            i = i + 1
        return result