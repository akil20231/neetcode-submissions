from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)

        rowLen, colLen = len(board), len(board[0])

        for i in range(rowLen):
            for j in range(colLen):
                item = board[i][j]
                if item == '.':
                    continue
                
                if item in row[i] or item in col[j] or item in square[(i // 3, j // 3)]:
                    return False
                
                else:
                    row[i].add(item)
                    col[j].add(item)
                    square[(i // 3, j // 3)].add(item)
        
        return True

        