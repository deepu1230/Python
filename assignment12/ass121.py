class MyClass:
    def _init_(self, arg1=None, arg2=None):
        if arg1 is None and arg2 is None:
            print("Default constructor called")
        elif arg2 is None:
            print(f"One-argument constructor called with arg1={arg1}")
        else:
            print(f"Two-argument constructor called with arg1={arg1} and arg2={arg2}")

class MainClass:
    def main(self):
        obj1 = MyClass()  # Default constructor
        obj2 = MyClass("Hello")  # One-argument constructor
        obj3 = MyClass("Hello", "World")  # Two-argument constructor

main_obj = MainClass()
main_obj.main()
