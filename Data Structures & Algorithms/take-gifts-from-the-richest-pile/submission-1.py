import heapq
import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        gifts = [-gift for gift in gifts]
        heapq.heapify(gifts)

        for _ in range(k):
            val = -heapq.heappop(gifts)
            val = int(val ** 0.5) 
            heapq.heappush(gifts, -val)

        return -sum(gifts)