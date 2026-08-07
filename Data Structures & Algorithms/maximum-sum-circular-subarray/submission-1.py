class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currMax, maxSum, currMin, minSum, total = float("-inf"), float("-inf"), float("inf"), float("inf"), 0

        for n in nums:
            currMax = max(n, currMax + n)
            maxSum = max(maxSum, currMax)

            currMin = min(n, currMin + n)
            minSum = min(minSum, currMin)

            total += n
        
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum
        
        