class Base:
    __name = ""
    def set(self, name):
        self.__name = name
    def get(self):
        print(self.__name)
ob = Base()
a = "xyz"
ob.set(a)
ob.get()