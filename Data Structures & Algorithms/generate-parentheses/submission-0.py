class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

    

        def backtrack(open_cnt, close_cnt, row):
            # Base Case
            if len(row) == 2 * n:
                res.append(row)
                return
            
            if open_cnt < n:
                backtrack(open_cnt + 1, close_cnt, row + "(")

            
            if close_cnt < open_cnt:
                backtrack(open_cnt, close_cnt + 1, row + ")")
            


        backtrack(0, 0, "")

        return res