class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        counts = Counter(nums)
        
        d, total = counts.most_common(1)[0]

        leftCount = 0
        leftLen = 0

        for i in range(n-1):
            if nums[i] == d:
                leftCount += 1

            rightCount = total - leftCount

            leftLen = i + 1
            rightLen = n - leftLen

            if (leftCount * 2 > leftLen) and (rightCount * 2 > rightLen):
                return i

        return -1
        
        


        
