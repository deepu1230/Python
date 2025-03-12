class Class2:
    def _init_(self, name, city):
        self.name = name
        self.city = city

    def method2(self):
        print(f"Hello from {self.name} in Class2")
        print(f"City: {self.city}")

    def display_details(self):
        print("Class2 Details:")
        print(f"Name: {self.name}")
        print(f"City: {self.city}")

