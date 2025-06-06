# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
      

        def isSame(root1, root2):
            if not root1 and not root2:
                return True
            
            if root1 and root2 and root1.val == root2.val:
                return isSame(root1.left, root2.left) and isSame(root1.right,root2.right)
            
            return False

            
        if not root:
            return False

        if isSame(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right,subRoot)