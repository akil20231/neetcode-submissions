class Solution:
    def inBetween(self, start, mid, end):
        return start < mid <= end



    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        if nums[0] >= n:
            return n

        prev = nums[0]

        for i in range(1, n):
            curr = nums[i]
            if curr == prev:
                continue
            total = n - i

            if self.inBetween(prev, total, curr):
                return total

            prev = curr

        return -1

