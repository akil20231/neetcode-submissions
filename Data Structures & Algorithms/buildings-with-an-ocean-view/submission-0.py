class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        stack = []

        for ind, val in enumerate(heights):

            while stack and heights[stack[-1]] <= val:
                stack.pop()
            
            stack.append(ind)

        return stack
            




            