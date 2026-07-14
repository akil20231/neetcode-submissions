class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n == 0:
            return [[]]

        res = []
        nums.sort()
        def backtrack(i, path):
            if i == n:
                res.append(path[:])
                return

            if i > n:
                return
            
            path.append(nums[i])
            backtrack(i+1, path)

            path.pop()

            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1
            
            backtrack(i + 1, path)

        backtrack(0, [])
        return res
