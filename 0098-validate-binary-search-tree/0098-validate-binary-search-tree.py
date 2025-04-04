# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        val = []
        def inorder(node):
            if not node:
                return 0
            inorder(node.left)
            val.append(node.val)
            
            inorder(node.right)
            
        
        inorder(root)
        print(val)
        for i in range(1, len(val)):
            if val[i] - val[i-1] <= 0:
                return False

        return True