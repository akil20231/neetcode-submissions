class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        out = []

        for num in arr:
            diff = abs(num - x)

            out.append((diff, num))
        
        closest = sorted(out)[:k]

        res = [num for _, num in closest]
        res.sort()
        return res


        

        
       
        