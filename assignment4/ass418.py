def remove_duplicates(array):
    new_array = []
    for num in array:
        if num not in new_array:
            new_array.append(num)
    return new_array