import heapq
import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        gifts = [-gift for gift in gifts]
        heapq.heapify(gifts)

        for _ in range(k):
            largest = -heapq.heappop(gifts)
            remaining = int(largest ** 0.5) 
            heapq.heappush(gifts, -remaining)

        return -sum(gifts)