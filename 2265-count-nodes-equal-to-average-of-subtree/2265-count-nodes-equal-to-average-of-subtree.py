# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   
    count = 0
    countNode = 0
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        def summ(root):
            if not root:
                return 0
            self.count += 1
            left_sum= root.val + summ(root.left)
            right_sum = summ(root.right)
            return left_sum + right_sum 
        
       
        def checkNode(node):
            if node == None:
                return 
            total = summ(node)
            average = floor(total/self.count)
            if average == node.val:
                self.countNode += 1
            self.count = 0
            checkNode(node.right)
            checkNode(node.left)
        checkNode(root)
        return self.countNode
            
       