class Node:
    def __init__(self, key=-1):
        self.key = key
        self.next = None
class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.data = [Node() for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        curr = self.data[self._hash(key)]

        while curr.next:
            if curr.next.key == key:
                return          # Already exists
            curr = curr.next

        curr.next = Node(key)

    def remove(self, key: int) -> None:
        curr = self.data[self._hash(key)]

        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next

    def contains(self, key: int) -> bool:
        curr = self.data[self._hash(key)].next

        while curr:
            if curr.key == key:
                return True
            curr = curr.next

        return False