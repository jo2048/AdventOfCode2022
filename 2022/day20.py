from util import readfile


class Node:
    def __init__(self, value, next, previous):
        self.value = value
        self.next = next
        if next is None:
            self.next = self
        self.previous = previous
        if previous is None:
            self.previous = self


class DLQueue:
    def __init__(self, values=()):
        self.start = None
        self.size = 0
        self.zero = None
        self.order = []
        for value in values:
            self.append(value)
    
    def append(self, value):
        self.size += 1
        if self.start is None:
            self.start = Node(value, None, None)
        else:
            node = Node(value, self.start, self.start.previous)
            self.start.previous.next = node
            self.start.previous = node

        self.order.append(self.start.previous)
        if value == 0:
            self.zero = self.start.previous
    
    def get(self, node: Node, i: int):
        i %= self.size
        while i > 0:
            node = node.next
            i -= 1
        return node

    def _get_insertion_node(self, node):
        i = node.value % (self.size - 1)
        if i > self.size / 2:
            i -= self.size
        while i > 0:
            node = node.next
            i -= 1
        while i < 0:
            node = node.previous
            i += 1
        return node

    def _remove(self, node):
        self.size -= 1
        if node is self.start:
            self.start = node.next
        node.previous.next = node.next
        node.next.previous = node.previous

    def _insert(self, node, destination):
        self.size += 1
        destination.next.previous = node
        node.next = destination.next
        destination.next = node
        node.previous = destination

    def sort(self):
        for i, node in enumerate(self.order):
            if node.value % (self.size - 1) != 0:
                other = self._get_insertion_node(node)
                self._remove(node)
                self._insert(node, other)

    def __str__(self):
        s = str(self.start.value)
        node = self.start.next
        while node is not self.start:
            s += ', ' + str(node)
            node = node.next
        return s


def day20(filepath: str, decryption_key: int, nb_mix: int) -> int:
    queue = DLQueue((int(x) * decryption_key for x in readfile(filepath)))
    for _ in range(nb_mix):
        queue.sort()

    a = queue.get(queue.zero, 1000)
    b = queue.get(a, 1000)
    c = queue.get(b, 1000)
    return a.value + b.value + c.value


if __name__ == "__main__":
    print(day20("inputs/day20.in", 1, 1))    
    print(day20("inputs/day20.in", 811589153, 10))
