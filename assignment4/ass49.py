def reverse_array(array):
    """
    Reverses an array of integer values.

    Args:
        array (list): The array to reverse.

    Returns:
        list: The reversed array.
    """
    return array[::-1]

# Example usage:
array = [1, 2, 3, 4, 5]
reversed_array = reverse_array(array)

print("Original array:", array)  # Output: Original array: [1, 2, 3, 4, 5]
print("Reversed array:", reversed_array)  # Output: Reversed array: [5, 4, 3, 2, 1]