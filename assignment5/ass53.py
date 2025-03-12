class MyClass:
    static_variable = "I'm a static variable"

obj = MyClass()
obj.static_variable = "Changed within instance"

print(MyClass.static_variable)  # Output: I'm a static variable
print(obj.static_variable)  # Output: Changed within instance