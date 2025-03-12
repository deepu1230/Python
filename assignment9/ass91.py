from abc import ABC, abstractmethod

class AbstractClass(ABC):
    def __init__(self):
        self.value = 10

    @abstractmethod
    def abstract_method(self):
        pass

    def non_abstract_method(self):
        print("Non-abstract method called")
        return self.value