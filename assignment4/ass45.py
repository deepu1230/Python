def remove_element(array, element):
    """
    Removes the first occurrence of the specified element from the array.

    Args:
        array (list): The array to remove the element from.
        element: The element to remove.

    Returns:
        list: The updated array with the element removed.
    """
    if element in array:
        array.remove(element)
    return array