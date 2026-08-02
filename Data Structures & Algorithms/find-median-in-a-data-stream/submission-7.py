class MedianFinder:

    def __init__(self):
        self.heap = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap,-num)

        

    def findMedian(self) -> float:
        heap = self.heap.copy()
        n = len(heap)

        if n % 2 != 0:
            for i in range(n // 2):
                heapq.heappop(heap)
            return -heapq.heappop(heap)
        else:
            for i in range(n//2 - 1):
                heapq.heappop(heap)
            mid1 = -heapq.heappop(heap)
            mid2 = -heapq.heappop(heap)
            return (mid1 + mid2) / 2

        
        