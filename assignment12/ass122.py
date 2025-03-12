class ParentClass:
    def _init_(self, arg1=None, arg2=None):
        if arg1 is None and arg2 is None:
            print("Parent default constructor called")
        elif arg2 is None:
            print(f"Parent one-argument constructor called with arg1={arg1}")
        else:
            print(f"Parent two-argument constructor called with arg1={arg1} and arg2={arg2}")

class ChildClass(ParentClass):
    def _init_(self, arg1=None, arg2=None):
        super()._init_(arg1, arg2)

class MainClass:
    def main(self):
        obj1 = ChildClass()  # Calls parent default constructor
        obj2 = ChildClass("Hello")  # Calls parent one-argument constructor
        obj3 = ChildClass("Hello", "World")  # Calls parent two-argument constructor

main_obj = MainClass()
main_obj.main()
