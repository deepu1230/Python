class MyClass:
    def my_method(self, *args):
        if len(args) == 1 and isinstance(args[0], int):
            print(f"my_method with one integer argument: {args[0]}")
        elif len(args) == 2 and isinstance(args[0], str) and isinstance(args[1], int):
            print(f"my_method with two arguments: {args[0]}, {args[1]}")
        else:
            print("Invalid arguments")

obj = MyClass()
obj.my_method(10)
obj.my_method("Hello", 20)

