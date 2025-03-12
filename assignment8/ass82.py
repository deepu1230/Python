class ProtectedClass:
    def __init__(self):
        self._protected_field = 20

    def _protected_method(self):
        print("Protected method called")

class SamePackageClass:
    def access_protected_members(self):
        obj = ProtectedClass()
        print(obj._protected_field)
        obj._protected_method()

class ChildClass(ProtectedClass):
    def access_protected_members(self):
        print(self._protected_field)
        self._protected_method()

obj = SamePackageClass()
obj.access_protected_members()

obj_child = ChildClass()
obj_child.access_protected_members()

