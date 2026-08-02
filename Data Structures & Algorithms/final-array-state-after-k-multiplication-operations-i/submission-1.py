import heapq
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        tuples = [(num, ind) for ind, num in enumerate(nums)]
        
        heapq.heapify(tuples)

        for i in range(k):
            num, ind = heapq.heappop(tuples)
            num *= multiplier
            nums[ind] = num
            heapq.heappush(tuples, (num, ind))
        
        return nums



