class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols=defaultdict(set)
        rows=defaultdict(set)
        squares=defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    continue
                
                elif board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in squares[(i//3,j//3)]:
                    return False
                
                else:
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    squares[(i//3,j//3)].add(board[i][j])
        print(len(cols),len(rows),len(squares))
        return True



        
