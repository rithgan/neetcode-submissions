class Node:
    def __init__(self, key=-1, value=-1):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.data = [Node() for _ in range(self.size)]

    def hash(self, key):
        return key % self.size

    def put(self, key, value):
        curr = self.data[self.hash(key)]

        while curr.next:
            if curr.next.key == key:
                curr.next.value = value
                return
            curr = curr.next

        curr.next = Node(key, value)

    def get(self, key):
        curr = self.data[self.hash(key)].next

        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next

        return -1

    def remove(self, key):
        curr = self.data[self.hash(key)]

        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next