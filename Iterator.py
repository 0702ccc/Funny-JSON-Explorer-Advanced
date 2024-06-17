from abc import ABC, abstractmethod


class Iterator(ABC):
    @abstractmethod
    def getNext(self):
        pass

    @abstractmethod
    def hasMore(self):
        pass


class Iterator_node(Iterator):
    def __init__(self, node):
        self.node = node
        self.count = 0

    def getNext(self):
        self.count += 1
        return self.node.children[self.count - 1], self.count == 1, self.count == len(self.node.children)

    def hasMore(self):
        return self.count < len(self.node.children)

class IteratorCollection(ABC):
    @abstractmethod
    def create_iterator(self):
        pass

class JSONIteratorCollection(IteratorCollection):
    def __init__(self, root):
        self.root = root

    def create_iterator(self):
        return Iterator_node(self.root)
