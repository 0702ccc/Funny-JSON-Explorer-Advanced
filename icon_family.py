import json

class IconFamily:
    """Class to manage icon families."""

    def __init__(self, icon_family):
        """
        Initialize the IconFamily.

        Args:
            icon_family (str): The name of the icon family.
        """
        # Load icon configuration from JSON file
        with open('config.json', 'r', encoding='utf-8') as f:
            self.icons = json.load(f)
        self.icon_family = icon_family

    def get_container_icon(self):
        """
        Get the icon for containers based on the specified icon family.

        Returns:
            str: The icon for containers.
        """
        return self.icons['icon_families'][self.icon_family]['icon_container']

    def get_leaf_icon(self):
        """
        Get the icon for leaves based on the specified icon family.

        Returns:
            str: The icon for leaves.
        """
        return self.icons['icon_families'][self.icon_family]['icon_leaf']
