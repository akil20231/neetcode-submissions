class Solution:
    def isVowel(self, c):
        return c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'

    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        res = []

        Q = len(queries)

        vowels = [self.isVowel(word[0]) and self.isVowel(word[-1]) for word in words]

        for li, ri in queries:
            count = 0
            for i in range(li, ri + 1):
                if vowels[i]:
                    count += 1 
            
            res.append(count)
        
        return res








        