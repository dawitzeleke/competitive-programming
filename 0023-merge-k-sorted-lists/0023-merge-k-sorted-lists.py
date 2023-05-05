# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = []
        
        for lis in lists:
        
            temp = lis
            while temp:
                heappush(heap, temp.val)
                temp = temp.next
                
        dummy = ListNode()
        ptr = dummy
        
        while heap:
            current = ListNode(heappop(heap))
            ptr.next = current
            ptr = ptr.next
           
        return dummy.next
            
        
        
                                