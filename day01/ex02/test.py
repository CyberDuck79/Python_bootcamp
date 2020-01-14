from vector import Vector

print("test initialisation :")
print("Vector([0.0, 1.0, 2.0, 3.0])")
print(Vector([0.0, 1.0, 2.0, 3.0]).value)
print("Vector(3)")
print(Vector(3).value)
print("Vector((10,45,15))")
print(Vector((10,45,15)).value)
print("Vector((10,15))")
print(Vector((10,15)).value)

print("test additions")
print("v = Vector([0.0, 1.0, 2.0, 3.0])")
v = Vector([0.0, 1.0, 2.0, 3.0])
print("v + 5")
v + 5
print(v.value)
v = Vector([0.0, 1.0, 2.0, 3.0])
print("5 + v")
5 + v
print(v.value)
print("v2 = Vector([0.0, 1.0, 2.0, 3.0])")
v2 = Vector([0.0, 1.0, 2.0, 3.0])
print("v + v2")
v + v2
print(v.value)
print("v2 = Vector([0.0, 1.0, 2.0, 3.0, 4.0])")
v2 = Vector([0.0, 1.0, 2.0, 3.0, 4.0])
try:
	print("v + v2")
	v + v2
except ValueError:
	print("error OK\n")

print("test de soustractions")
print("v = Vector([0.0, 1.0, 2.0, 3.0])")
v = Vector([0.0, 1.0, 2.0, 3.0])
print("v - 5")
test = v - 5
print(test)
v = Vector([0.0, 1.0, 2.0, 3.0])
print("5 - v")
5 - v
print(v.value)
print("v2 = Vector([0.0, 1.0, 2.0, 3.0])")
v2 = Vector([0.0, 1.0, 2.0, 3.0])
print("v - v2")
v - v2
print(v.value)
print(v2.value)
v2 = Vector([0.0, 1.0, 2.0, 3.0])
print("v2 - v")
v2 - v
print(v.value)
print(v2.value)
print("v2 = Vector([0.0, 1.0, 2.0, 3.0, 4.0])")
v2 = Vector([0.0, 1.0, 2.0, 3.0, 4.0])
try:
	print("v - v2")
	v - v2
except ValueError:
	print("error OK\n")

print("test de divisions")
print("v = Vector([0.0, 1.0, 2.0, 3.0])")
v = Vector([0.0, 1.0, 2.0, 3.0])
print("v / 5")
test = v / 5
print(test)
v = Vector([0.0, 1.0, 2.0, 3.0])
print("5 / v")
5 / v
print(v.value)
try:
	print("v / v2")
	v / v2
except ValueError:
	print("error OK\n")

print("test de multiplications")
print("v = Vector([0.0, 1.0, 2.0, 3.0])")
v = Vector([0.0, 1.0, 2.0, 3.0])
print("v * 5")
test = v * 5
print(test)
v = Vector([0.0, 1.0, 2.0, 3.0])
print("5 * v")
5 * v
print(v.value)
print("v2 = Vector([0.0, 1.0, 2.0, 3.0])")
v2 = Vector([0.0, 1.0, 2.0, 3.0])
print("v * v2")
test = v * v2
print(test)
v2 = Vector([0.0, 1.0, 2.0, 3.0])
print("v2 * v")
test = v2 * v
print(test)
print("v2 = Vector([0.0, 1.0, 2.0, 3.0, 4.0])")
v2 = Vector([0.0, 1.0, 2.0, 3.0, 4.0])
try:
	print("v * v2")
	v - v2
except ValueError:
	print("error OK\n")

print(v)
print(repr(v))