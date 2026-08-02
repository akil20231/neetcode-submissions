import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [(-cnt, char) for char, cnt in count.items()]
        heapq.heapify(maxHeap)

        prev = None
        res = ""

        while maxHeap:
            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1          

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            if cnt != 0:
                prev = (cnt, char)

        if prev:
            return ""

        return res





        
