class PrivateClass:
    def __init__(self):
        self.__private_field = 10

    def __private_method(self):
        print("Private method called")

    def main(self):
        print(self.__private_field)
        self.__private_method()

class PrivateSubClass(PrivateClass):
    def access_private_members(self):
        # Cannot access private_field directly
        # print(self.__private_field)

        # Cannot access private_method directly
        # self.__private_method()

        # Using name mangling
        print(self._PrivateClass__private_field)
        self._PrivateClass__private_method()

obj = PrivateClass()
obj.main()

obj_sub = PrivateSubClass()
obj_sub.access_private_members()
