class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums) // 3
        res = []
        hash_table = Counter(nums)

        for key, value in hash_table.items():
            if value > n:
                res.append(key)
        
        return res

    
        