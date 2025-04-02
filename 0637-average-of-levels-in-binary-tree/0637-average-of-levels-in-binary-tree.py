# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        queue = deque([root])

        res = []

        while(queue):
            size = len(queue)
            current_level = 0

            for _ in range(size):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                print(node.val)
                current_level += node.val
            
            res.append(current_level / size)
        
        return res