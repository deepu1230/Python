def contains_value(array, value):
    """
    Checks if the given array contains the specified value.

    Args:
        array (list): The array to search in.
        value: The value to search for.

    Returns:
        bool: True if the array contains the value, False otherwise.
    """
    return value in array

# Example usage:
array = [1, 2, 3, 4, 5]
value = 3

result = contains_value(array, value)
print(f"Array contains {value}: {result}")  # Output: Array contains 3: True