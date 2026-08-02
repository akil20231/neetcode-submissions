class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        directions = [
            (1, 0),    # down
            (-1, 0),   # up
            (0, 1),    # right
            (0, -1)    # left
        ]

        def dfs(r, c, i):
            # Base Case
            if i == len(word):
                return True
            
            if not (0 <= r < rows and 0 <= c < cols) or (board[r][c] != word[i]):
                return False
            
            temp = board[r][c]
            board[r][c] = "#"

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if dfs(nr, nc, i + 1):
                    return True

            board[r][c] = temp

            return False

        
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True

        return False
