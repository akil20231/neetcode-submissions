class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        l = 0
        t_wind = Counter(t)
        s_wind = Counter()

        have = 0
        need = len(t_wind)

        res, resLen = [-1, -1], float("inf")

        for r in range(len(s)):
            s_wind[s[r]] += 1

            if s[r] in t_wind and s_wind[s[r]] == t_wind[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)

                s_wind[s[l]] -= 1
                if s[l] in t_wind.keys() and s_wind[s[l]] < t_wind[s[l]]:
                    have -= 1
                l += 1

        l, r = res   

            
        return s[l: r + 1] if resLen != float("inf") else ""

        
            
            





        


        
       
        

        
        

        

        