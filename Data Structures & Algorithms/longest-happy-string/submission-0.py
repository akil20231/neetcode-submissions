import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a:
            heap.append((-a, "a"))
        if b:
            heap.append((-b, "b"))
        if c:
            heap.append((-c, "c"))

        heapq.heapify(heap)

        res = []

        while heap:
            cnt1, char1 = heapq.heappop(heap)

            if len(res) >= 2 and res[-1] == res[-2] == char1:
                if not heap:
                    break

                cnt2, char2 = heapq.heappop(heap)
                res.append(char2)
                cnt2 += 1 

                if cnt2 != 0:
                    heapq.heappush(heap, (cnt2, char2))

                heapq.heappush(heap, (cnt1, char1))

            else:
                res.append(char1)
                cnt1 += 1

                if cnt1 != 0:
                    heapq.heappush(heap, (cnt1, char1))

        return "".join(res)
