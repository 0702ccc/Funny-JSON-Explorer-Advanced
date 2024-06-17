from abc import ABC, abstractmethod

class Component(ABC):
    """Abstract base class for components."""

    @abstractmethod
    def add_child(self, child):
        """Add a child component."""
        pass

    @abstractmethod
    def draw(self, level, is_first, is_last, parent_is_last, icon):
        """Draw the component."""
        pass


class Leaf(Component):
    """Leaf component represents individual items in the tree."""

    def add_child(self, child):
        """Leaf components cannot have children."""
        pass

    @abstractmethod
    def draw(self, level, is_first, is_last, parent_is_last, icon):
        """Draw the leaf component."""
        pass


class TreeStyleLeaf(Leaf):
    """Leaf component for tree-style output."""

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def draw(self, level, is_first, is_last, parent_is_last, icon):
        """Draw the leaf component in tree style."""
        # Calculate indentation based on the component's level and parent hierarchy
        indent = ""
        for i in range(level - 1):
            if parent_is_last[i]:
                indent += "    "
            else:
                indent += "│   "

        # Determine the connector based on whether it's the last component in the level
        connector = "└─" if is_last else "├─"
        # Construct the line to be printed
        line = f"{indent}{connector}{icon.get_leaf_icon()}{self.name}"
        # Append value if available
        if self.value is not None:
            line += f": {self.value}"
        # Print the line
        print(line)


class RectangleStyleLeaf(Leaf):
    """Leaf component for rectangle-style output."""

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def draw(self, level, is_first, is_last, parent_is_last, icon):
        """Draw the leaf component in rectangle style."""
        # Calculate indentation and connector based on the component's level and parent hierarchy
        indent = ""
        flag = True
        for i in range(level - 1):
            if not parent_is_last[i]:
                flag = False
            indent += "│   "
        if flag and is_last:
            indent = '└───'
            for i in range(level - 2):
                indent += '───'
        connector = "┴─" if flag and is_last else "├─"
        subfix = '┘' if flag and is_last else '┤'
        # Construct the prefix for the line to be printed
        if self.value is not None:
            prefix = indent + connector + icon.get_leaf_icon()
            # Print the line with value
            print(f"{prefix}{self.name}: {self.value} " + '─' * (43 - len(prefix) - len(self.name) - len(self.value)) + subfix)
        else:
            prefix = indent + connector + icon.get_leaf_icon()
            # Print the line without value
            print(f"{prefix}{self.name} " + '─' * (45 - len(prefix) - len(self.name)) + subfix)


class Container(Component):
    """Container component represents the branches in the tree."""

    def __init__(self):
        self.children = []

    def add_child(self, child):
        """Add a child component to the container."""
        self.children.append(child)

    @abstractmethod
    def draw(self, level, is_first, is_last, parent_is_last, icon):
        """Draw the container component."""
        pass


class TreeStyleContainer(Container):
    """Container component for tree-style output."""

    def __init__(self, name, level):
        super().__init__()
        self.name = name
        self.level = level

    def draw(self, level, is_first, is_last, parent_is_last, icon):
        """Draw the container component in tree style."""
        # Calculate indentation and connector based on the component's level and parent hierarchy
        indent = ""
        for i in range(level - 1):
            indent += "│   " if not parent_is_last[i] else "    "

        connector = "└─" if is_last else "├─"
        # Print the container name with appropriate indentation and connector
        print(f"{indent}{connector}{icon.get_container_icon()}{self.name}")
        parent_is_last.append(is_last)
        # Recursively draw children components
        for i, child in enumerate(self.children):
            child.draw(level + 1, i == 0, i == len(self.children) - 1, parent_is_last, icon)
        parent_is_last.pop()


class RectangleStyleContainer(Container):
    """Container component for rectangle-style output."""

    def __init__(self, name, level):
        super().__init__()
        self.name = name
        self.level = level

    def draw(self, level, is_first, is_last, parent_is_last, icon):
        """Draw the container component in rectangle style."""
        # Calculate indentation and connector based on the component's level and parent hierarchy
        indent = ""
        for i in range(level - 1):
            indent += "│   " if not parent_is_last[i] else "    "
        connector = "┌─" if level == 1 and is_first else "├─"
        subfix = '┐' if level == 1 and is_first else '┤'
        prefix = indent + connector + icon.get_container_icon()
        print(f"{prefix}{self.name} " + '─' * (45 - len(prefix) - len(self.name)) + subfix)
        parent_is_last.append(is_last)
        for i, child in enumerate(self.children):
            child.draw(level + 1, i == 0, i == len(self.children) - 1, parent_is_last, icon)
        parent_is_last.pop()

