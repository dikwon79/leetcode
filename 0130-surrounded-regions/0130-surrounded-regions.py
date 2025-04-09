class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows , cols = len(board), len(board[0])
        def dfs(a,b):
            if a<0 or a>=rows or b<0 or b>=cols or board[a][b] !='O':
                return 

            board[a][b] = "E"
            dfs(a+1,b)
            dfs(a-1,b)
            dfs(a,b+1)
            dfs(a,b-1)

        for i in range(rows):
            for j in [0, cols-1]:
                if board[i][j] == "O":
                    dfs(i,j)
        
        for j in range(cols):
            for i in [0, rows-1]:
                if board[i][j] == "O":
                    dfs(i,j)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "E":
                    board[i][j] = "O"

        