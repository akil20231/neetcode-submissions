class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        a = Counter(arr)
        arr = [item for item in a if a[item] == 1]

        return arr[k - 1] if k <= len(arr) else ""

        
