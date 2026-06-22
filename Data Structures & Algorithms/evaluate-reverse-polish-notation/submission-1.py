class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        stack = []
        operators = {"+", "-", "*", "/"}
        for i in range(n):
            if tokens[i] not in operators:
                stack.append(tokens[i])
            else:
                second = int(stack.pop())
                first = int(stack.pop())

                if tokens[i] == "+":
                    stack.append(first + second)
                elif tokens[i] == "-":
                    stack.append(first - second)
                elif tokens[i] == "*":
                    stack.append(first * second)
                elif tokens[i] == "/":
                    stack.append(first / second)

        return int(stack[0])

