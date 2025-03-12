class PublicClass:
    def __init__(self):
        self.public_field = 30

    def public_method(self):
        print("Public method called")

class SamePackageClass:
    def access_public_members(self):
        obj = PublicClass()
        print(obj.public_field)
        obj.public_method()

class DifferentPackageClass:
    def access_public_members(self):
        obj = PublicClass()
        print(obj.public_field)
        obj.public_method()

obj = SamePackageClass()
obj.access_public_members()

obj_diff = DifferentPackageClass()
obj_diff.access_public_members()