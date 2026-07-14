class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res, sol = [], []

        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return
            
            if i > n:
                return
            
           
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

            j = i + 1
            while j < n and nums[j] == nums[i]:
                j += 1
            
            backtrack(j)
        
        backtrack(0)
        return res
