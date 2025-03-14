# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        def symmetric(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False

            return (a.val == b.val and symmetric(a.left, b.right) and symmetric(a.right, b.left))
        
        return symmetric(root.left, root.right)

        