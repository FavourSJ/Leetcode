class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = []
        count = 0

        for ch in s:
            if ch == "(":
                res.append(ch)
                count += 1
            elif ch == ")" and count > 0:
                res.append(ch)
                count -= 1
            elif ch != ")":
                res.append(ch)

        filtered = []
        for ch in res[::-1]:
            if ch == "(" and count > 0:
                count -= 1
            else:
                filtered.append(ch)

        return "".join(filtered[::-1])