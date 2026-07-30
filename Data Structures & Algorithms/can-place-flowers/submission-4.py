class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        for i in range(len(flowerbed)):
            prev = flowerbed[i - 1] == 0 if i - 1 >= 0 else True
            pos = flowerbed[i + 1] == 0 if i + 1 < len(flowerbed) else True
            if prev and flowerbed[i] == 0 and pos:
                n -= 1
                flowerbed[i] = 1
                if n == 0:
                    return True
                    
        return False
        

        
        

        