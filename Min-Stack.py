class MinStack:

    def __init__(self):
        self.p = []
        self.m = 9999999999999
    def push(self, x):
        self.p.append(x)
        self.m=min(self.m,x)
    def pop(self):
        tem=self.p.pop()
        if tem==self.m:
            if self.p:
                self.m=min(self.p)
            else:
                self.m=9999999999999
    def top(self):
        return self.p[-1]

    def getMin(self):
        if self.p:
            return self.m
        else:
            return None
