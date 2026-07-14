class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        nums = candidates

        nums.sort()
        res, sub = [], []
        
        def backtrack(i, total):
            if total == target:
                res.append(sub.copy())
                return
            
            if total > target or i >= n:
                return
            
            sub.append(nums[i])
            backtrack(i+1, total + nums[i])
            sub.pop()

            j = i + 1
            while j < n and nums[j] == nums[i]:
                j += 1
            
            backtrack(j, total)
        
        backtrack(0, 0)

        return res