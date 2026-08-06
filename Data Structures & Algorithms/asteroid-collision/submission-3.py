class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        stack = []

        for i in range(n):
            curr = asteroids[i]

            if curr < 0:
                
                while stack and stack[-1] > 0 and abs(curr) > stack[-1]:
                    stack.pop()
                
                if stack and stack[-1] > 0 and abs(curr) <= abs(stack[-1]):
                    if abs(curr) == abs(stack[-1]):
                        stack.pop()
                    continue
                
            
            stack.append(curr)

            




        return stack

