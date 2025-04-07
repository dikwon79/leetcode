class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])

        count = 0

        def dfs(p, q):
            if p < 0 or p >= rows or q <0 or q >= cols or grid[p][q]=='0':
                return 
            grid[p][q] = '0'
            dfs(p+1,q)
            dfs(p-1,q)
            dfs(p,q+1)
            dfs(p,q-1)   
        

        for p in range(rows):
            for q in range(cols):
                if grid[p][q] == "1":
                    dfs(p,q)
                    count += 1

        return count 
