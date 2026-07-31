class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s_list = list(s)
        remove = set()
        open_count = 0

        for i, ch in enumerate(s_list):
            if ch == '(':
                open_count += 1
            elif ch == ')':
                if open_count == 0:
                    remove.add(i)
                else:
                    open_count -= 1


        for i in range(len(s_list) - 1, -1, -1):
            if open_count == 0:
                break

            if s_list[i] == '(':
                remove.add(i)
                open_count -= 1

        return "".join(
            ch for i, ch in enumerate(s_list)
            if i not in remove
        )
            
        



