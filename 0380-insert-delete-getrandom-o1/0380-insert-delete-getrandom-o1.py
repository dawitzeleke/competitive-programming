class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.hashmap = {}
        self.length = len(self.arr)

    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            return False
        self.hashmap[val] = self.length
        self.arr.append(val)
        self.length += 1
        return True

    def remove(self, val: int) -> bool:
        # check if val exists
        if val not in self.hashmap:
            return False
        # swap the val with the last entry in the arr

        val_index = self.hashmap[val]
        last_num = self.arr[-1]

        self.arr[val_index], self.arr[-1] = self.arr[-1], self.arr[val_index]

        self.hashmap[last_num] = val_index

        self.arr.pop()
        del self.hashmap[val]
        self.length -= 1
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()