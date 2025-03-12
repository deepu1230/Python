class MyClass:
    def my_method(self, *args):
        if len(args) == 1:
            print(f"my_method with one argument: {args[0]}")
        elif len(args) == 2:
            print(f"my_method with two arguments: {args[0]}, {args[1]}")
        else:
            print("Invalid number of arguments")

obj = MyClass()
obj.my_method("Hello")
obj.my_method("Hello", "World")

