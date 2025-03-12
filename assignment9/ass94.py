class NonAbstractClass:
    def __init__(self):
        self.value = 50

    def non_abstract_method(self):
        print("Non-abstract method called")

class ChildClass:
    def __init__(self):
        self.non_abstract_obj = NonAbstractClass()

    def call_non_abstract_method(self):
        self.non_abstract_obj.non_abstract_method()