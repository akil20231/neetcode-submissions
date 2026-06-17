class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        L, R = 0, m*n - 1

        while L <= R:
            mid = (L+R) // 2
            i , j = mid // n, mid % n

            if target == matrix[i][j]:
                return True
            elif matrix[i][j] < target:
                L = mid + 1
            else:
                R = mid - 1
        
        return False




        
        