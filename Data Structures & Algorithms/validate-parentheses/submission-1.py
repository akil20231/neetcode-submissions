class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)

        stack = []
        p_map = {
            '}' : '{',
            ')' : '(',
            ']' : '['
        }

        for ch in s:
            if ch in p_map:
                if not stack or stack[-1] != p_map[ch]:
                    return False
                stack.pop()

            else:
                stack.append(ch)

        return not stack


            


                



        