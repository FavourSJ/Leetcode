class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []

        for i in range(1, n+1):
            newList = ""

            if i % 3 == 0:
                newList += "Fizz"
            if i % 5 == 0:
                newList += "Buzz"
            if i % 3 != 0 and i % 5 != 0:
                newList += f'{i}'

            answer.append(newList)
        return answer
        