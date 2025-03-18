# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        root = postorder.pop()

        result = TreeNode(root)

        key = inorder.index(root)

        result.right = self.buildTree(inorder[key+1:], postorder)

        result.left = self.buildTree(inorder[:key], postorder)
        

        return result
        
       