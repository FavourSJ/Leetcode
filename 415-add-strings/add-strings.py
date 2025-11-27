class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        result = []  # build digits in reverse order

        # Process from the end of each string until both are done and no carry remains
        while i >= 0 or j >= 0 or carry:
            x = int(num1[i]) if i >= 0 else 0
            y = int(num2[j]) if j >= 0 else 0
            total = x + y + carry
            carry = total // 10
            digit = total % 10
            result.append(str(digit))
            i -= 1
            j -= 1

        # Since we appended least significant digits first, reverse the list
        return ''.join(reversed(result))