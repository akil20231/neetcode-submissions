class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set()
        duplicate = -1
        missing = -1

        for row in grid:
            n = len(row)

            for num in row:
                if num in seen:
                    duplicate = num
                seen.add(num)
        
        for num in range(1, n * n + 1):
            if num not in seen:
                missing = num
                break




        return [duplicate, missing]