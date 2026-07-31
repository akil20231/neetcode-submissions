class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = []
        hash_dict = {}

        for n in nums2:
            if not stack:
                stack.append(n)
            else: 
                if stack[-1] < n:
                    while stack and stack[-1] < n:
                        val = stack.pop()
                        hash_dict[val] = n
                    
                    stack.append(n)
                else:
                    stack.append(n)
        
        while stack:
            val = stack.pop()
            hash_dict[val] = -1
        
        res = []
        for num in nums1:
            res.append(hash_dict[num])
        return res
                
                


                



        
        


        