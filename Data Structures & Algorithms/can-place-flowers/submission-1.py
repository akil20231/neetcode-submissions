class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        empty = 0 if flowerbed[0] else 1
        print(empty)
        for f in flowerbed:
            if f:
                n -= int((empty - 1) / 2)
                empty = 0
            else:
                empty += 1

            print(empty)
        
        n -= (empty) // 2

        return n <= 0
        

        
        

        