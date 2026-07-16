class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        hash_table = Counter(nums)

        for key, value in hash_table.items():
            if value > n // 3:
                res.append(key)
        
        return res

    
        