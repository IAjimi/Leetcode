class Solution:
    def isValid(self, s: str) -> bool:
        """
        Runtime: 52 ms, faster than 27.72% of Python3 online submissions for Valid Parentheses.
        Memory Usage: 13.9 MB, less than 94.44% of Python3 online submissions for Valid Parentheses."""
        matching = {"{": "}", "(": ")", "[": "]"}
        stack = []

        for char in s:
            if char in matching:
                stack.append(char)
            else:  # only ()[]{} allowed in str
                if not stack:
                    return False

                open_char = stack.pop()
                if char != matching[open_char]:
                    return False

        if stack:
            return False
        return True


if __name__ == "__main__":
    assert not Solution().isValid("(")
    assert not Solution().isValid("}")
    assert Solution().isValid("()")
    assert not Solution().isValid("(]")
    assert Solution().isValid("([{}])")
    assert not Solution().isValid("([{})")
    assert not Solution().isValid("([{})")
