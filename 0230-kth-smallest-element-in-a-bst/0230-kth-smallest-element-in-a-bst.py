# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        inorder_val = []

        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            inorder_val.append(node.val)
            inorder(node.right)
        
        inorder(root)

        small_value = float('inf')

        for i in range(len(inorder_val)):
            small_value = min(small_value, k**inorder_val[i])
        
        return small_value