gender = input("Enter gender (M/F): ")

switch = {
    'M': 'Male',
    'F': 'Female'
}

print(switch.get(gender.upper(), "Invalid input"))