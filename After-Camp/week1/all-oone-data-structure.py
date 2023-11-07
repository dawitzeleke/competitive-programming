from sortedcontainers import SortedList
class AllOne:

    def __init__(self):
        self.count = defaultdict(int)
        self.ans = SortedList()

    def inc(self, key: str) -> None:
        count = self.count[key]
        if count > 0:
            self.ans.remove((count, key))
        self.count[key] += 1
        self.ans.add((count + 1, key))

    def dec(self, key: str) -> None:
        count = self.count[key]
        if count > 0:
            self.ans.remove((count, key))
        self.count[key] -= 1
        if self.count[key] > 0:
            self.ans.add((count - 1, key))
    def getMaxKey(self) -> str:
        if len(self.ans) == 0:
            return ""
        return self.ans[-1][1]

    def getMinKey(self) -> str:
        if len(self.count) == 0:
            return ""
        return self.ans[0][1]


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()