class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = []
        # count the number of unmatched '('
        count = 0

        # first pass to remove the invalid ')'
        for ch in s:
            if ch == "(":
                # need to track the unmatched '('
                res.append(ch)
                count += 1
            elif ch == ")" and count > 0:
                # match ')' with an opening '('
                res.append(ch)
                count -= 1
            elif ch != ")":
                # just add normal letters
                res.append(ch)

        # second passing through remove any extra '('
        filtered = []
        # iterate through backwards so from right to left
        for ch in res[::-1]:
            if ch == "(" and count > 0:
                count -= 1
            else:
                filtered.append(ch)

        # return everything but reverse back to the correct order
        return "".join(filtered[::-1])