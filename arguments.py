from typing import Any, Optional, List

def add_to_list(item: Any, target_list: Optional[List[Any]] = None) -> List[Any]:
    """
    Appends an item to a target list if provided. Creates a new list if no list is provided.

    Args:
        item (Any): An item to add to a list.
        target_list (Optional[List[Any]]): The list to add the item to. If None, a new list is created.

    Returns:
        List[any]: The provided list with item appended or a new list with item if no list was provided.

    Example:
        >>> add_to_list(1)
        [1]
        >>> add_to_list(4, [2])
        [2, 4]
    """
    if target_list is None:
        # Create a new list and return item in it.
        return [item] # Pythonic to create new list while returning
    else:
        # List was provided
        target_list.append(item)
        return target_list