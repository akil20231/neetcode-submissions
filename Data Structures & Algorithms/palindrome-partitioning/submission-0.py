class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(word):
            return word == word[::-1]

        def backtrack(i, row):

            # Base case
            if i == len(s):
                res.append(row.copy())
                return

            # Try every substring choice
            for j in range(i, len(s)):

                substring = s[i:j+1]

                # Only choose palindromes
                if isPalindrome(substring):

                    # Take the choice
                    row.append(substring)

                    # Explore the next choices
                    backtrack(j + 1, row)

                    # Undo the choice
                    row.pop()

        backtrack(0, [])

        return res
