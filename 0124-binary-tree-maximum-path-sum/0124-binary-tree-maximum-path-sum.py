# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:


    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        result = root.val

        def dfs(node):
            nonlocal result
            if not node: 
                return 0
            
            left_max = max(dfs(node.left),0)
            right_max = max(dfs(node.right),0)
            
            sum_level = left_max + node.val + right_max


            result = max(result, sum_level)
            
            return node.val + max(left_max, right_max)

             
        
        dfs(root)
       
        return result