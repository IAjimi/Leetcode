class MinStack:
    """
    Runtime: 54 ms, faster than 98.16% of Python3 online submissions for Min Stack.
    Memory Usage: 18.3 MB, less than 28.31% of Python3 online submissions for Min Stack.
    """

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            prev_min = self.stack[-1][1]
            new_min = min(val, prev_min)
            self.stack.append((val, new_min))
        else:
            self.stack.append((val, val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
