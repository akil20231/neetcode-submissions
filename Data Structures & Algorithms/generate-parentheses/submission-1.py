class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(open_cnt, close_cnt, row):
            # Base Case
            if len(row) == 2 * n:
                res.append("".join(row))
                return
            
            if open_cnt < n:
                row.append("(")
                backtrack(open_cnt + 1, close_cnt, row)
                row.pop()

            
            if close_cnt < open_cnt:
                row.append(")")
                backtrack(open_cnt, close_cnt + 1, row)
                row.pop()
            


        backtrack(0, 0, [])

        return res