class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        seen = set(nums)

        for num in nums:
            if num - 1 not in seen:
                next_num = num + 1
                length = 1
                while next_num in seen:
                    length += 1
                    next_num += 1
                count = max(count, length)
            
        return count
        
        