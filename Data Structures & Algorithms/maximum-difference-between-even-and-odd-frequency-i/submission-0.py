class Solution:
    def maxDifference(self, s: str) -> int:
        count = Counter(s)

        maxOdd = 0
        minEven = float("inf")

        for freq in count.values():
            if freq % 2 == 1:
                maxOdd = max(maxOdd, freq)
            else:
                minEven = min(minEven, freq)

        return maxOdd - minEven



