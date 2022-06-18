# Leetcode: https://leetcode.com/problems/lru-cache/submissions/

class LinkedList:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.tail = None
        self.list = None
        self.cache = {}
        self.capacity = capacity

    def remove_node(self, key):
        if key not in self.cache:
            return
        
        # get node from cache
        node = self.cache.pop(key)

        # handle a single node in the linked-list
        if node.prev == None and node.next == None:
            return

        # handle a head node in the linked-list
        if node.prev == None and node.next != None:
            self.list = self.list.next
            return

        # handle last node in the linked-list
        if node.next == None:
            self.tail = node.prev

            if self.tail != None:
                self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        return

    def get(self, key: int) -> int:
        node = self.cache.get(key, None)

        if node == None:
            return -1

        value = node.value
        self.put(node.key, value)

        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if self.capacity == 1:
            self.cache = {key: LinkedList(key, value)}
            return

        l = LinkedList(key, value)
        self.remove_node(key)

        if self.list == None:
            self.list = l
            self.tail = l
            self.cache[key] = l
            return

        if len(self.cache) + 1 > self.capacity:
            self.cache.pop(self.tail.key)
            self.tail = self.tail.prev
            
            if self.tail != None:
                self.tail.next = None
        
        # refer cache to the node
        self.cache[key] = l

        # move latest node to head
        l.next = self.list
        self.list.prev = l
        self.list = l
