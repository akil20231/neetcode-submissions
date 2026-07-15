class Solution:
    def scoreOfString(self, s: str) -> int:
        n = len(s)
        total = 0
        prev = ord(s[0])
        for i in range(1, n):
            total += abs(ord(s[i]) - prev)
            prev = ord(s[i])
        
        return total

        