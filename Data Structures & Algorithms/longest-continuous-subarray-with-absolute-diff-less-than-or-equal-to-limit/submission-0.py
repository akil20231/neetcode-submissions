class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minQ = deque() # mono inc
        maxQ = deque() # mono dec
        l = 0
        res = 0

        for r in range(len(nums)):
            while minQ and nums[r] < minQ[-1]:
                minQ.pop()
            while maxQ and nums[r] > maxQ[-1]:
                maxQ.pop()

            minQ.append(nums[r])
            maxQ.append(nums[r])

            while minQ and maxQ and maxQ[0] - minQ[0] > limit:
                if nums[l] == maxQ[0]:
                    maxQ.popleft()
                if nums[l] == minQ[0]:
                    minQ.popleft()
                l += 1

            res = max(res, r-l+1)

        print(maxQ)
        print(minQ)



        return res








