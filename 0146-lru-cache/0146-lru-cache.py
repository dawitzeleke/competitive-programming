class ListNode:
    def __init__(self, key= -1, value= -1, prev= None, next= None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):

        self.LRUCache = defaultdict(ListNode)
        self.size = capacity
        self.MRU = ListNode()
        self.LRU = ListNode()

        self.MRU.next = self.LRU
        self.LRU.prev = self.MRU
        print(self.LRUCache)

    def remove(self, node):
        next_node = node.next
        prev_node = node.prev

        prev_node.next = next_node
        next_node.prev = prev_node

    def addToFront(self, node):
        MRU_next = self.MRU.next
        self.MRU.next = node
        node.prev = self.MRU
        node.next = MRU_next
        MRU_next.prev = node

    def get(self, key: int) -> int:
        if key not in self.LRUCache:
            return -1
        curr_node = self.LRUCache[key]
        self.remove(curr_node)
        self.addToFront(curr_node)
        return curr_node.value

        

    def put(self, key: int, value: int) -> None:

        if key in self.LRUCache:
            curr_node = self.LRUCache[key]
            curr_node.value = value
            self.remove(curr_node)
            self.addToFront(curr_node)

        else:
            if len(self.LRUCache) == self.size:
                LRU = self.LRU.prev
                self.remove(LRU)
                del self.LRUCache[LRU.key]
            node = ListNode(key, value)
            self.addToFront(node)
            self.LRUCache[key] = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)