class Solution:
    def processString(self, string: str) -> str:
        stack = []

        for char in string:
            if stack and char == "#":
                stack.pop()
            elif char != "#":
                stack.append(char)

        return "".join(stack)

    def backspaceCompare(self, s: str, t: str) -> bool:
        """
        Runtime: 33 ms, faster than 78.92% of Python3 online submissions for Backspace String Compare.
        Memory Usage: 13.9 MB, less than 85.54% of Python3 online submissions for Backspace String Compare.
        """
        string1 = self.processString(s)
        string2 = self.processString(t)
        return string1 == string2
