def find_duplicates(array):
    """
    Finds duplicate values in an array.

    Args:
        array (list): The array to find duplicates in.

    Returns:
        list: A list of duplicate values.
    """
    seen = set()
    duplicates = set()

    for value in array:
        if value in seen:
            duplicates.add(value)
        seen.add(value)

    return list(duplicates)

# Example usage:
array = [1, 2, 3, 2, 4, 5, 5, 6]
duplicates = find_duplicates(array)

print("Duplicate values:", duplicates)  # Output: Duplicate values: [2, 5]