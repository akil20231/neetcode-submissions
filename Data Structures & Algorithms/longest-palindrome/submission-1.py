class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 1:
            return 1

        counts = Counter(s)

        ans = 0

        for freq in counts.values():
            ans += freq // 2 * 2

        if ans < len(s):
            ans += 1

        return ans


        