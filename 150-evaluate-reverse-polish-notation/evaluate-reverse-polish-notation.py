class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t in "+-*/":
                b, a = stack.pop(), stack.pop()

                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(a - b)
                elif t == "*":
                    stack.append(a * b)
                else:
                    if a / b < 0:
                        stack.append(ceil(a / b))
                    else:
                        stack.append(floor(a / b))

            else:
                stack.append(int(t))

        return stack[0]
