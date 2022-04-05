class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = [set() for _ in range(9)]
        for i in range(9):
            row = set()
            if i%3==0:
                box = [set() for _ in range(3)]
            for j in range(9):
                if board[i][j]!=".":
                    if board[i][j] in row:
                        # print(1, i, j, board[i][j])
                        return False
                    else:
                        row.add(board[i][j])
                    if board[i][j] in col[j]:
                        # print(2, i, j, board[i][j])
                        return False
                    else:
                        col[j].add(board[i][j])
                    if board[i][j] in box[j//3]:
                        # print(3, i, j, board[i][j])
                        return False
                    else:
                        box[j//3].add(board[i][j])
        return True
            