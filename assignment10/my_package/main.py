from my_package import Class1, Class2

def main():
    print("Creating objects and calling methods:")
    obj1 = Class1("John", 30)
    obj1.method1()
    obj1.display_details()

    obj2 = Class2("Alice", "New York")
    obj2.method2()
    obj2.display_details()

    print("\nAccessing class attributes:")
    print(Class1._name_)
    print(Class2._name_)

    print("\nChecking instance types:")
    print(isinstance(obj1, Class1))
    print(isinstance(obj2, Class2))

if __name__ == "_main_":
    main()
