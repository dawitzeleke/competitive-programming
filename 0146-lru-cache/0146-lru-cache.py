class DoublyLinkedList:
    def __init__(self, key, value, next = None, prev = None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.MRU = DoublyLinkedList(-1, -1)
        self.LRU = DoublyLinkedList(-1, -1)
        self.MRU.next = self.LRU
        self.LRU.prev = self.MRU
    
    def remove(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
    def addToFront(self, node):
        MRUnext = self.MRU.next
        self.MRU.next = node
        node.prev = self.MRU
        node.next = MRUnext
        MRUnext.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            currNode = self.cache[key]
            self.remove(currNode)
            self.addToFront(currNode)
            return currNode.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.cache[key].value = value
            self.remove(self.cache[key])
            self.addToFront(self.cache[key])
            
        else:
            if len(self.cache) == self.capacity:
                nodeToDelete = self.LRU.prev
                self.remove(nodeToDelete)
                del self.cache[nodeToDelete.key]
            
            node = DoublyLinkedList(key, value)
            self.cache[key] = node
            self.addToFront(node)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)