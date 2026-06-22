from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n1 = len(s1)
        n2 = len(s2)

        for i in range(n2 - n1 + 1):
            sub_2 = s2[i:n1+i] 

            if (Counter(s1) == Counter(sub_2)):
                return True


        return False
        