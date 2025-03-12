class MyClass:
    static_variable = "I'm a static variable"

MyClass.static_variable = "Changed within class"

obj = MyClass()
print(MyClass.static_variable)  # Output: Changed within class
print(obj.static_variable)  # Output: Changed within class