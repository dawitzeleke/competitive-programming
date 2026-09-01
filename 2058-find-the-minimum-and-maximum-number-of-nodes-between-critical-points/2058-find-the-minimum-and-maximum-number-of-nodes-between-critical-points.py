class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        criticalPts = []  
        prev = head
        curr = head.next
        pos = 1  

        while curr.next:
            # 1. Traverse and find points
            if (curr.val > prev.val and curr.val > curr.next.val) or (curr.val < prev.val and curr.val < curr.next.val):
                criticalPts.append(pos)  # Record position of critical points
            prev = curr
            curr = curr.next
            pos += 1  

        if len(criticalPts) < 2:
            return [-1, -1]

        # 2. Calculate Distances
        minDist = float('inf')
        maxDist = criticalPts[-1] - criticalPts[0]

        for i in range(1, len(criticalPts)):
            minDist = min(minDist, criticalPts[i] - criticalPts[i - 1])  # Find the minimum distance

        # Return the result
        return [minDist, maxDist]