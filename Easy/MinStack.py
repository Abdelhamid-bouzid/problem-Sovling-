class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l   = [] 
        self.min = float("inf")

    def push(self, x: int) -> None:
        if x<self.min:
            self.min=x
        self.l.append(x)
        
    def pop(self) -> None:
        self.l.pop()
        if len(self.l)==0:
            self.min = float("inf")
        else:
            self.min = min(self.l)
        
    def top(self) -> int:
        return self.l[-1]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
