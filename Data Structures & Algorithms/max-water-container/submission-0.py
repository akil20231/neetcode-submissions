class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_width = 0
        max_height = 0
        max_area = 0
        l,r = 0, n-1

        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            area = width * height
            max_area = max(area, max_area)
            if (heights[l] < heights[r]):
                l += 1
            elif (heights[l] >  heights[r]):
                r -= 1
            else:
                l += 1
                r -= 1
        
        return max_area
            



            
        

            




