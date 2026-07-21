class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = len(strs)
        longest = strs[0]
        for i in range(1, s):
            current = strs[i]
            j = 0

            while j < min(len(longest), len(current)):
                if longest[j] != current[j]:
                    break
                j += 1
            longest = longest[:j]
        return longest
            
            


            


        
