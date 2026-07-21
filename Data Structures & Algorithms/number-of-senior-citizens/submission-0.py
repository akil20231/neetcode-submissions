class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        n = len(details)
        for i in range(n):
            age = int(details[i][11:13])

            if age > 60:
                count += 1
        
        return count