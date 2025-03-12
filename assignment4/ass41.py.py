def sum_array_integers(arr):  
  """  
  Calculates the sum of integer values in an array (list).  

  Args:  
    arr: A list (array) of numbers.  Non-integer values will be ignored.  

  Returns:  
    The sum of the integer values in the array.  Returns 0 if the array is empty or contains no integers.  
  """  
  total = 0  
  for element in arr:  
    if isinstance(element, int):  # Check if the element is an integer  
      total += element  
  return total