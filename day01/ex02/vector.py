
class Vector:

	def __init__(self, value):
		if isinstance(value, list):
			self.value = list(map(float, value))
			self.size = len(value)
		elif isinstance(value, tuple):
			if len(value) == 2:
				self.value = list(map(float, range(value[0],value[1])))
				self.size = len(self.value)
			else:
				self.value = list(map(float, value))
				self.size = len(value)
		elif isinstance(value, int):
			self.size = value
			self.value = list(map(float, range(0,value)))
	
	def __add__(self, other):
		if isinstance(other, int) or isinstance(other, float):
			for i, elem in enumerate(self.value):
				self.value[i] = elem + other
		elif isinstance(other, Vector):
			if other.size != self.size:
				raise ValueError("the two vectors lust be the same size")
			for i, elem in enumerate(self.value):
				self.value[i] = elem + other.value[i]
		return self.value
	__radd__ = __add__

	def __sub__(self, other):
		if isinstance(other, int) or isinstance(other, float):
			for i, elem in enumerate(self.value):
				self.value[i] = elem - other
		elif isinstance(other, Vector):
			if other.size != self.size:
				raise ValueError("the two vectors lust be the same size")
			for i, elem in enumerate(self.value):
				self.value[i] = elem - other.value[i]
		return self.value
	__rsub__ = __sub__

	def __truediv__(self, other):
		if isinstance(other, int) or isinstance(other, float):
			if other == 0:
				raise ZeroDivisionError("erreur division par 0")
			for i, elem in enumerate(self.value):
				self.value[i] = elem / other
		elif isinstance(other, Vector):
			raise ValueError("vector div error")
		return self.value
	__rtruediv__ = __truediv__

	def __mul__(self, other):
		if isinstance(other, int) or isinstance(other, float):
			for i, elem in enumerate(self.value):
				self.value[i] = elem * other
			return self.value
		elif isinstance(other, Vector):
			if other.size != self.size:
				raise ValueError("the two vectors lust be the same size")
			product = 0
			for i, elem in enumerate(self.value):
				product += elem * other.value[i]
			return product
	__rmul__ = __mul__

	def __str__(self):
		return f"{self.value}"
	
	def __repr__(self):
		return f"size : {self.size}, {self.value}"
