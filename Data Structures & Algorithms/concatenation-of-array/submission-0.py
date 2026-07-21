class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        x = 2*n
        ans = [0] * x

        for i in range(n):
            ans[i] = nums[i]

        j = 0

        for i in range(n, len(ans)):
            ans[i] = nums[j]
            j += 1
        return ans

            




        