from json_node import *
from Iterator import *


class Product(ABC):
    """Abstract base class for products."""

    def __init__(self):
        self._container = None
        self._leaf = None
        self._my_container = None

    @abstractmethod
    def set_container(self):
        """Set the container type."""
        pass

    @abstractmethod
    def set_leaf(self):
        """Set the leaf type."""
        pass

    def _load(self, data):
        """Load the data into the product."""
        self._my_container = self._container('root', 0)
        stack = [(self._my_container, data)]
        while stack:
            current_container, current_data = stack.pop()
            for key, value in current_data.items():
                if isinstance(value, dict):
                    new_container = self._container(key, current_container.level + 1)
                    current_container.add_child(new_container)
                    stack.append((new_container, value))
                else:
                    leaf = self._leaf(key, value)
                    current_container.add_child(leaf)

    def show(self, icon, data):
        """Display the product."""
        self._load(data)
        parent_is_last = []
        iterator_collection = JSONIteratorCollection(self._my_container)
        iter = iterator_collection.create_iterator()
        while iter.hasMore():
            child, first, last = iter.getNext()
            child.draw(self._my_container.level + 1, first, last, parent_is_last, icon)


class TreeStyleProduct(Product):
    """Product for tree-style output."""

    def set_container(self):
        """Set the container type for tree style."""
        self._container = TreeStyleContainer

    def set_leaf(self):
        """Set the leaf type for tree style."""
        self._leaf = TreeStyleLeaf


class RectangleStyleProduct(Product):
    """Product for rectangle-style output."""

    def set_container(self):
        """Set the container type for rectangle style."""
        self._container = RectangleStyleContainer

    def set_leaf(self):
        """Set the leaf type for rectangle style."""
        self._leaf = RectangleStyleLeaf
