# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count = defaultdict(int)
        def helper(root):
            if not root:
                return 
            count[root.val] += 1
            helper(root.right)
            helper(root.left)
            
        helper(root)
        maximum = max(count.values())
        answer = []
        for num in count:
            if count[num] == maximum:
                answer.append(num)
        return answer