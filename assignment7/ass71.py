# Super class A
class A:
    def _init_(self):
        self.a = 10

    def method_a1(self):
        print("Method A1 in class A")

    def method_a2(self):
        print("Method A2 in class A")

    def override_method(self):
        print("Override method in class A")

# Sub class B of A
class B(A):
    def _init_(self):
        super()._init_()
        self.b = 20

    def method_b1(self):
        print("Method B1 in class B")

    def method_b2(self):
        print("Method B2 in class B")

    def override_method(self):
        print("Override method in class B")

# Sub class C of B
class C(B):
    def _init_(self):
        super()._init_()
        self.c = 30

    def method_c1(self):
        print("Method C1 in class C")

    def method_c2(self):
        print("Method C2 in class C")

    def override_method(self):
        print("Override method in class C")

# Main class
class Main:
    def main(self):
        # Create objects
        obj_a = A()
        obj_b = B()
        obj_c = C()

        # Call methods using objects
        print("Class A methods:")
        obj_a.method_a1()
        obj_a.method_a2()
        obj_a.override_method()

        print("\nClass B methods:")
        obj_b.method_a1()
        obj_b.method_a2()
        obj_b.method_b1()
        obj_b.method_b2()
        obj_b.override_method()

        print("\nClass C methods:")
        obj_c.method_a1()
        obj_c.method_a2()
        obj_c.method_b1()
        obj_c.method_b2()
        obj_c.method_c1()
        obj_c.method_c2()
        obj_c.override_method()

        # Runtime polymorphism with method overriding
        print("\nRuntime polymorphism with method overriding:")
        obj_b_ref = B()
        obj_c_ref = C()

        A.override_method(obj_b_ref)  # Calls override_method in class B
        A.override_method(obj_c_ref)  # Calls override_method in class C

        # Runtime polymorphism with data members
        print("\nRuntime polymorphism with data members:")
        print("obj_a.a =", obj_a.a)  # Accesses data member 'a' of class A
        print("obj_b.a =", obj_b.a)  # Accesses data member 'a' of class A through object of class B
        print("obj_b.b =", obj_b.b)  # Accesses data member 'b' of class B
        print("obj_c.a =", obj_c.a)  # Accesses data member 'a' of class A through object of class C
        print("obj_c.b =", obj_c.b)  # Accesses data member 'b' of class B through object of class C
        print("obj_c.c =", obj_c.c)  # Accesses data member 'c' of class C

if '__name__' == "_main_":
    main_obj = Main()
    main_obj.main()# Super class A
class A:
    def _init_(self):
        self.a = 10

    def method_a1(self):
        print("Method A1 in class A")

    def method_a2(self):
        print("Method A2 in class A")

    def override_method(self):
        print("Override method in class A")

# Sub class B of A
class B(A):
    def _init_(self):
        super()._init_()
        self.b = 20

    def method_b1(self):
        print("Method B1 in class B")

    def method_b2(self):
        print("Method B2 in class B")

    def override_method(self):
        print("Override method in class B")

# Sub class C of B
class C(B):
    def _init_(self):
        super()._init_()
        self.c = 30

    def method_c1(self):
        print("Method C1 in class C")

    def method_c2(self):
        print("Method C2 in class C")

    def override_method(self):
        print("Override method in class C")

# Main class
class Main:
    def main(self):
        # Create objects
        obj_a = A()
        obj_b = B()
        obj_c = C()

        # Call methods using objects
        print("Class A methods:")
        obj_a.method_a1()
        obj_a.method_a2()
        obj_a.override_method()

        print("\nClass B methods:")
        obj_b.method_a1()
        obj_b.method_a2()
        obj_b.method_b1()
        obj_b.method_b2()
        obj_b.override_method()

        print("\nClass C methods:")
        obj_c.method_a1()
        obj_c.method_a2()
        obj_c.method_b1()
        obj_c.method_b2()
        obj_c.method_c1()
        obj_c.method_c2()
        obj_c.override_method()

        # Runtime polymorphism with method overriding
        print("\nRuntime polymorphism with method overriding:")
        obj_b_ref = B()
        obj_c_ref = C()

        A.override_method(obj_b_ref)  # Calls override_method in class B
        A.override_method(obj_c_ref)  # Calls override_method in class C

        # Runtime polymorphism with data members
        print("\nRuntime polymorphism with data members:")
        print("obj_a.a =", obj_a.a)  # Accesses data member 'a' of class A
        print("obj_b.a =", obj_b.a)  # Accesses data member 'a' of class A through object of class B
        print("obj_b.b =", obj_b.b)  # Accesses data member 'b' of class B
        print("obj_c.a =", obj_c.a)  # Accesses data member 'a' of class A through object of class C
        print("obj_c.b =", obj_c.b)  # Accesses data member 'b' of class B through object of class C
        print("obj_c.c =", obj_c.c)  # Accesses data member 'c' of class C

if '__name__'== "_main_":
    main_obj = Main()
    main_obj.main()