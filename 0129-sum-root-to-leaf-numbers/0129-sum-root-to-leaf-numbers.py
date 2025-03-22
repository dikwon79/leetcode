# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        total = 0
        queue = deque([(root, 0)])

        while(queue):
            node, current_sum = queue.popleft() 

            if not node.left and not node.right:
                total += current_sum + node.val
            
            if node.left:
                queue.append((node.left, (current_sum + node.val) * 10))
            if node.right:
                queue.append((node.right,(current_sum + node.val) * 10))
        
        return total