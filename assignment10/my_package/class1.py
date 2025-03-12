class Class1:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    def method1(self):
        print(f"Hello from {self.name} in Class1")
        print(f"Age: {self.age}")

    def display_details(self):
        print("Class1 Details:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
