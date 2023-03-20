# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        count = defaultdict(int)
        def helper(node):
            if not node:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            temp = left + right + node.val

            count[temp] += 1


            return temp
        helper(root)
        
        ans = max(count.values())
        res = []
        for key in count:
            if count[key] == ans:
                res.append(key)
        return res