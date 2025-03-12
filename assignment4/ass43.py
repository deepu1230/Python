def find_index(arr, element):  
  """  
  Finds the index of a given element in an array (list) without using try-except.  

  Args:  
    arr: The list (array) to search in.  
    element: The element to search for.  

  Returns:  
    The index of the element in the array if found.  
    Returns -1 if the element is not found.  
  """  
  for i in range(len(arr)):  
    if arr[i] == element:  
      return i  # Element found at index i  
  return -1  # Element not found  

# Example usage (same as before)  
my_array = [10, 20, 30, 40, 50]  

# Element found  
index = find_index(my_array, 30)  
if index != -1:  
  print("Element 30 found at index:", index)  
else:  
  print("Element 30 not found in the array")  

# Element not found  
index = find_index(my_array, 60)  
if index != -1:  
  print("Element 60 found at index:", index)  
else:  
  print("Element 60 not found in the array")  

# Example with strings:  
string_array = ["apple", "banana", "cherry"]  
index = find_index(string_array, "banana")  
if index != -1:  
    print("Element 'banana' found at index:", index)  
else:  
    print("Element 'banana' not found in the array")