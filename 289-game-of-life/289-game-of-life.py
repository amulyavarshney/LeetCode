class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])
        new_board = [[0]*n for _ in range(m)]
        d = [(0,1), (1,0), (0,-1), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)]
        for i in range(m):
            for j in range(n):
                c = 0
                for dx,dy in d:
                    x, y = i+dx, j+dy
                    if 0<=x<m and 0<=y<n and board[x][y]==1:
                        c += 1
                if board[i][j]==1:
                    if c==2 or c==3:
                        new_board[i][j] = 1
                else:
                    if c == 3:
                        new_board[i][j] = 1
        for i in range(m):
            for j in range(n):
                board[i][j] = new_board[i][j]
                    
                    