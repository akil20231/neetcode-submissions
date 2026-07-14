class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n == 0:
            return [[]]

        res = []
        path = []
        nums.sort()

        def backtrack(i):
            if i == n:
                res.append(path[:])
                return

            if i > n:
                return
            
            path.append(nums[i])
            backtrack(i+1)

            path.pop()

            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1
            
            backtrack(i + 1)

        backtrack(0)
        return res
