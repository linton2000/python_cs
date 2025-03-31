# https://leetcode.com/problems/min-stack/description/

# Final Sol - Two Stacks (checked sols)
class MinStack:

    def __init__(self):
        self.lst = []
        self.minLst = []

    def push(self, val: int) -> None:
        self.lst.append(val)

        minVal = val
        if self.minLst:
            minVal = min(val, self.minLst[-1])
        self.minLst.append(minVal)

    def pop(self) -> None:
        self.lst.pop()
        self.minLst.pop()

    def top(self) -> int:
        return self.lst[-1]

    def getMin(self) -> int:
        return self.minLst[-1]

# Final Sol - One Stack (checked sols)
class MinStack:

    def __init__(self):
        self.lst = []
        self.minVal = 0

    def push(self, val: int) -> None:
        if not self.lst:
            self.lst.append(0)
            self.minVal = val
        else:
            self.lst.append(val - self.minVal)
            self.minVal = min(val, self.minVal)

    def pop(self) -> None:
        pop = self.lst.pop()
        if pop < 0:
            self.minVal = self.minVal - pop

    def top(self) -> int:
        if self.lst[-1] > 0:
            return self.minVal + self.lst[-1]
        else:
            return self.minVal

    def getMin(self) -> int:
        return self.minVal
    