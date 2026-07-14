class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)

        if n == 1:
            if nums[0] != target:
                return []
            else:
                return nums[0]
        
        res, sol = [], []

        def backtrack(i, cur_sum):
            if cur_sum == target:
                res.append(sol.copy())
                return

            if cur_sum > target or i == n:
                return
            
            backtrack(i + 1, cur_sum)

            sol.append(nums[i])
            backtrack(i, cur_sum + nums[i])
            sol.pop()
        
        backtrack(0, 0)

        return res


        

        
        