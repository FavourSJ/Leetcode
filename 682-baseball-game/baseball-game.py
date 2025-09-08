class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []

        for i in operations:
            if i == "+":
                scores.append(scores[-1] + scores[-2])
            elif i == "D":
                scores.append(scores[-1] * 2)
            elif i == "C":
                scores.pop()
            else:
                scores.append(int(i))

        return sum(scores)
        