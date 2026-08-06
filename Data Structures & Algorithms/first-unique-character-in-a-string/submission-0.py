class Solution:
    def firstUniqChar(self, s: str) -> int:

        counts = Counter(s)

        for idx, val in counts.items():
            if val == 1:
                return s.find(idx)
        return -1


