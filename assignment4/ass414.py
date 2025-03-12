def find_second_largest(array):
    if len(array) < 2:
        return None
    array.sort()
    return array[-2]