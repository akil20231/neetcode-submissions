class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        indices = sorted(range(len(heights)), key=lambda i: heights[i], reverse=True)

        return [names[i] for i in indices]
        
        