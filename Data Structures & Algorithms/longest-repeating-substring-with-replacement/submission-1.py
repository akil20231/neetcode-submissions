from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        if k == n:
            return k
        
        
        l = 0
        r = 0
        count = defaultdict(int)
        res = 0

        while l <= r and r < n:
            count[s[r]] += 1

            while (r-l+1) - max(count.values()) > k:
                print(max(count.values()))
                count[s[l]] -= 1
                l += 1


            res = max(res, r - l + 1)
            r += 1
            
        return res
            




        







        
        