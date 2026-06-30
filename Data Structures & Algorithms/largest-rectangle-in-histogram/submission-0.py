class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        maxArea = 0

        for i, height in enumerate(heights):
            start = i
            while stack and height < stack[-1][0]:
                h, j = stack.pop()
                w = i - j
                maxArea = max(maxArea, h*w)
                start = j
            
            stack.append((height, start))
        
        while stack:
            h, j = h, j = stack.pop()
            w = n - j
            maxArea = max(maxArea, h*w)
            
       
        
        return maxArea
