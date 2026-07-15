from collections import Counter
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)

        if s == '': return True

        if s_len > t_len:
            return False

        j = 0

        for i in range(t_len):
            if t[i] == s[j]:
                if j == s_len - 1:
                    return True
                j += 1
                
        return False

        

                    
                    


        




        