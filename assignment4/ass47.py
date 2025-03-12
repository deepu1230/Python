def insert_element(array, element, position):
    """
    Inserts an element at a specific position in the array.

    Args:
        array (list): The array to insert the element into.
        element: The element to insert.
        position (int): The position to insert the element at.

    Returns:
        list: The updated array with the element inserted.
    """
    if position < 0 or position > len(array):
        raise IndexError("Position out of range")
    array.insert(position, element)
    return array