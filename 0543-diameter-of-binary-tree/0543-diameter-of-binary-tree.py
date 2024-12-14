# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best = 0

        def dbs(root):
            if not root:
                return 0
            
            nonlocal best
            dbs_left = dbs(root.left)
            dbs_right = dbs(root.right)
           
            best = max(best, dbs_left + dbs_right)

            return max(dbs_left , dbs_right) + 1


        dbs(root)
        return best
