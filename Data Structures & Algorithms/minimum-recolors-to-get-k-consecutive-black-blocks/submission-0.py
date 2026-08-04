class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        
        counts = Counter()

        l, res = 0, float("inf")

        for r in range(n):
            counts[blocks[r]] += 1
            

            if r - l + 1 == k:
                res = min(res, counts["W"])
                counts[blocks[l]] -= 1
                l += 1



        return res

        