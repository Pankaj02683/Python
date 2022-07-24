class Base:
	def _init_(self):
		self._a = 2
class Derived(Base):
	def _init_(self):
		Base._init_(self)
obj1 = Derived()
print("Accessing protected member of obj1: ", obj1._a)