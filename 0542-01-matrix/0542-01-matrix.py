class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        queue = deque()

        result = [[float('inf')]* cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    result[r][c] = 0
                    queue.append((r,c))
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        while queue:
            r,c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <=nc < cols:
                    if result[nr][nc] > result[r][c] + 1:
                        result[nr][nc] = result[r][c] + 1
                        queue.append((nr, nc))
        
        return result



