class MyClass:
    def _init_(self):
        pass

    def __private_init(self):  # Name mangling for private constructor
        pass

    def _protected_init(self):  # Single underscore prefix for protected constructor
        pass

class MainClass:
    def main(self):
        obj = MyClass()
        # obj.__private_init()  # Raises AttributeError
        obj._protected_init()  # Accessible

main_obj = MainClass()
main_obj.main()
