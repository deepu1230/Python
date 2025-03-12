def find_min_max(array):
    """
    Finds the minimum and maximum value of an array.

    Args:
        array (list): The array to find the minimum and maximum value of.

    Returns:
        tuple: A tuple containing the minimum and maximum value.
    """
    if not array:
        raise ValueError("Array is empty")

    min_value = array[0]
    max_value = array[0]

    for value in array:
        if value < min_value:
            min_value = value
        elif value > max_value:
            max_value = value

    return min_value, max_value