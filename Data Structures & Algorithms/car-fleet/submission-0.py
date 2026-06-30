class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)

        pair = [(p,s) for p, s in zip(position, speed)]
        
        stack = [] 
        for p,s in sorted(pair):
            print((p,s))
            time = (target - p) / s

            while stack and time >= stack[-1]:
                stack.pop()

            stack.append(time)
        
        
        
        return len(stack)
        

        
        