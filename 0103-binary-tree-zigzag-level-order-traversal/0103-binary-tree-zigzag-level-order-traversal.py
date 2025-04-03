# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root])
        res = []
        level = 1
        while(queue):
            level_size = len(queue)
            
            current_level= []

            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
                current_level.append(node.val)

            if level % 2 == 0:
                res.append(current_level[::-1])
            else:
                res.append(current_level)

            level += 1

        return res