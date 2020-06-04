class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []
        

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append(x)
            self.min.append(x)
        else:
            self.stack.append(x)
            curr_min = self.min[-1]
            if x < curr_min:
                self.min.append(x)
            else:
                self.min.append(curr_min)
        

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()