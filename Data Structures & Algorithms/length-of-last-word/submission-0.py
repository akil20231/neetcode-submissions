class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        S = len(s)
        count = 0

        for i in range(len(s)-1, -1, -1):
            if not s[i].isalnum() and count > 0:
                break
            
            if s[i].isalnum():
                count += 1
        
        return count
                
            

        