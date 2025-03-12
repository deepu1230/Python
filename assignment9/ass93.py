class AbstractClass:
    def __init__(self):
        self.value = 40

    def abstract_method(self):
        print("Abstract method implemented")

class ChildClass:
    def __init__(self):
        self.abstract_obj = AbstractClass()

    def call_abstract_method(self):
        self.abstract_obj.abstract_method()
