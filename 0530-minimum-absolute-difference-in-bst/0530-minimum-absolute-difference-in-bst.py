# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        inorder_val = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            inorder_val.append(node.val)
            inorder(node.right) 
        
        inorder(root)
        difference = float('inf')
        for i in range(1,len(inorder_val)):
            difference = min( difference, inorder_val[i] - inorder_val[i-1])
        
        return difference