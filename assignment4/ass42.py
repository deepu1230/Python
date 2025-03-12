def average_array_integers(arr):  
  """  
  Calculates the average of integer values in an array (list) using sum(), len() and a generator.  

  Args:  
    arr: A list (array) of numbers.  Non-integer values will be ignored.  

  Returns:  
    The average of the integer values in the array.  
    Returns 0 if the array is empty or contains no integers.  
  """  
  integers = [element for element in arr if isinstance(element, int)] # Create a list of only integers  

  if not integers: # check if the integers list is empty  
    return 0  

  return sum(integers) / len(integers)  


# Example usage (same as before):  
my_array = [1, 2, 3, 4, 5]  
average = average_array_integers(my_array)  
print("Average of integers in the array:", average)  

my_array = [1, 2.5, 3, "hello", 4]  
average = average_array_integers(my_array)  
print("Average of integers in the array:", average)  

my_array = []  
average = average_array_integers(my_array)  
print("Average of integers in the array:", average)