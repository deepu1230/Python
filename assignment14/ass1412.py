class MyClass:
    def _init_(self):
        self.existent_field = "Hello, World!"

def generate_no_such_field_exception():
    obj = MyClass()
    try:
        print(obj.non_existent_field)
    except AttributeError:
        print("Attribute error handled")

generate_no_such_field_exception()