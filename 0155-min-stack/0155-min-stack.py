class MinStack:

    def __init__(self):
        self.minStack = []

    def push(self, val: int) -> None:
        curr_min = min(val, self.minStack[-1][1] if self.minStack else float("inf"))
        self.minStack.append([val, curr_min])
    def pop(self) -> None:
        self.minStack.pop()

    def top(self) -> int:
        return self.minStack[-1][0]

    def getMin(self) -> int:
        return self.minStack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()