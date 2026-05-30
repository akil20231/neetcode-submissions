class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        if n <= 3:
            if n < 3:
                return []
            return [nums] if nums[0] + nums[1] + nums[2] == 0 else []
        
        nums.sort()
        output = []

        for i in range(n):
            if i >= n - 2:
                break
            
            if nums[i] <= 0 and i < n - 2:
                j = i + 1
                k = n - 1
                while j < k:
                    total = nums[i] + nums[j] + nums[k]
                    if total == 0:
                        if [nums[i], nums[j], nums[k]] not in output:
                            output.append([nums[i], nums[j], nums[k]])
                        j += 1
                        k -= 1
                    elif total < 0:
                        j += 1
                    else:
                        k -= 1

            if nums[i] > 0:
                return output if len(output) != 0 else []
        
        return output if len(output) != 0 else []



        

        

           


        