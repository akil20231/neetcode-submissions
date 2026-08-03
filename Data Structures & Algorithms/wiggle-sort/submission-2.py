class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        less = True
        n = len(nums)
        i = 0
        j = 1

        while i < n and j < n:
            if less:
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
                less = False
                continue
            else:
                if nums[i] < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
                less = True
                continue
        
                

                
