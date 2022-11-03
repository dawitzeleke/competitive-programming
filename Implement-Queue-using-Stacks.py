class MyQueue:

    def __init__(self):
        self._stack1 = []
        self._stack2 = []
        self._length = 0

    def push(self, x):
        self._stack1.append(x)
        self._length += 1
        return None

    def pop(self):
        if self._stack2:
            self._length -= 1
            return self._stack2.pop()
        else:
            while self._stack1:
                self._stack2.append(self._stack1.pop())
            if self._stack2:
                self._length -= 1
                return self._stack2.pop()
            else:
                raise Exception()

    def peek(self):
        if self._stack2:
            return self._stack2[-1]
        else:
            while self._stack1:
                self._stack2.append(self._stack1.pop())
            if self._stack2:
                return self._stack2[-1]
            else:
                raise Exception()

    def empty(self):
        return not bool(self._length)
