from abc import ABC, abstractmethod
from json_product import *


class Strategy(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def execute_container(self):
        pass

    @abstractmethod
    def execute_leaf(self):
        pass


class Strategy_tree(Strategy):
    def __init__(self):
        self.product = TreeStyleProduct()

    def execute(self):
        """Get the result of the tree style factory."""
        return self.product

    def execute_container(self):
        """Create a container component for tree style."""
        self.product.set_container()

    def execute_leaf(self):
        """Create a leaf component for tree style."""
        self.product.set_leaf()


class Strategy_rectangle(Strategy):
    def __init__(self):
        self.product = RectangleStyleProduct()

    def execute(self):
        """Get the result of the tree style factory."""
        return self.product

    def execute_container(self):
        """Create a container component for tree style."""
        self.product.set_container()

    def execute_leaf(self):
        """Create a leaf component for tree style."""
        self.product.set_leaf()


class Context:
    def __init__(self, strategy: Strategy = None):
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy

    def execute_strategy(self):
        if self._strategy is None:
            raise ValueError("Strategy not set")
        self._strategy.execute_container()
        self._strategy.execute_leaf()
        return self._strategy.execute()
