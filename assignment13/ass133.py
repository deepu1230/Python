class MyClass:
    def my_method(self, arg1, arg2):
        if isinstance(arg1, int) and isinstance(arg2, int):
            print(f"my_method with two integer arguments: {arg1}, {arg2}")
        elif isinstance(arg1, str) and isinstance(arg2, str):
            print(f"my_method with two string arguments: {arg1}, {arg2}")
        else:
            print("Invalid arguments")

obj = MyClass()
obj.my_method(10, 20)
obj.my_method("Hello", "World")