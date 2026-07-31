class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        cnt = {}

        for c in arr:
            if c not in cnt:
                cnt[c] = 0
            cnt[c] += 1

        ndistinct = 0
        for c, v in cnt.items():
            if v == 1:
                ndistinct += 1
                if ndistinct == k:
                    return c

        return ""

        
