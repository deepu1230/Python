def find_common_values(array1, array2):
    """
    Finds common values between two arrays.

    Args:
        array1 (list): The first array.
        array2 (list): The second array.

    Returns:
        list: A list of common values.
    """
    return list(set(array1) & set(array2))

# Example usage:
array1 = [1, 2, 3, 4, 5]
array2 = [4, 5, 6, 7, 8]
common_values = find_common_values(array1, array2)

print("Common values:", common_values)  # Output: Common values: [4, 5]