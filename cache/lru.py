# Leetcode: https://leetcode.com/problems/lru-cache/submissions/

class LinkedList:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.node = {}
        self.capacity = capacity

        self.head = LinkedList(None, None)
        self.tail = LinkedList(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key not in self.node:
            return -1

        value = self.node[key].value
        self.put(key, value)

        return value

    def put(self, key, value):
        if key in self.node:
            self.remove(key)
            self.put(key, value)
            return
        
        node = LinkedList(key, value)
        temp_next = self.head.next
        
        self.head.next = node
        node.next = temp_next
        node.prev = self.head
        temp_next.prev = node

        if len(self.node) + 1 > self.capacity:
            self.remove(self.tail.prev.key)

        self.node[key] = node

    def remove(self, key):
        node = self.node[key]
        self.node.pop(key)
        node.prev.next = node.next
        node.next.prev = node.prev


if __name__ == '__main__':
    cache = LRUCache(4)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(3, 3)
    cache.put(4, 4)
    cache.put(5, 5)
    
    assert cache.get(1) == -1
    assert cache.get(2) == 2
    assert cache.get(4) == 4
    assert [cache.head.next.key, cache.head.next.next.key, cache.head.next.next.next.key, cache.head.next.next.next.next.key] == [4, 2, 5, 3]
