class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close2Open = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        for c in s:
            if c in close2Open:
                if stack and stack[-1] == close2Open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
        