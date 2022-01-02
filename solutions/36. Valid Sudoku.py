class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        squares = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                if i not in rows:
                    rows[i] = [board[i][j]]
                elif board[i][j] in rows[i]:
                    return False
                else:
                    rows[i].append(board[i][j])
                if j not in cols:
                    cols[j] = [board[i][j]]
                elif board[i][j] in cols[j]:
                    return False
                else:
                    cols[j].append(board[i][j])
                square = (i//3, j//3)
                if square not in squares:
                    squares[square] = [board[i][j]]
                elif board[i][j] in squares[square]:
                    return False
                else:
                    squares[square].append(board[i][j])
                    
                
        return True
            
