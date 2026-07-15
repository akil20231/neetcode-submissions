class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        S = len(s)
        T = len(t)

        j = 0

        remaining = T

        for i in range(S):
            if s[i] == t[j]:
                if j == T - 1:
                    remaining -= 1
                    break
                    
                j += 1
                remaining -= 1
                
        
        return remaining
        
        



    