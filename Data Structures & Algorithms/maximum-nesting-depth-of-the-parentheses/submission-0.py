class Solution:
    def maxDepth(self, s: str) -> int:
        
        res = 0

        stack = []

        for c in s:
            if c == "(":
                stack.append(c)
                res = max(res, len(stack))
            
            if c == ")":
                stack.pop()
                res = max(res, len(stack))
        
        return res