from abc import ABC, abstractmethod

class AbstractClass(ABC):
    def __init__(self):
        self.value = 10

    @abstractmethod
    def abstract_method(self):
        pass

class ChildClass(AbstractClass):
    def __init__(self):
        super().__init__()

    def abstract_method(self):
        print("Abstract method implemented in ChildClass")
