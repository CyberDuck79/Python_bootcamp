import sys

def usage():
	print("Usage: python operations.py <number1> <number2>")
	print("Example:")
	print("\tpython operations.py 10 3")
	quit()

if (len(sys.argv) < 3):
	usage()
elif (len(sys.argv) > 3):
	print("InputError: too many arguments\n")
	usage()
else:
	try:
		nb1 = int(sys.argv[1])
		nb2 = int(sys.argv[2])
	except:
		print("InputError: only numbers\n")
		usage()
print("Sum:\t\t{}".format(nb1 + nb2))
print("Difference:\t{}".format(nb1 - nb2))
print("Product:\t{}".format(nb1 * nb2))
if (nb2 == 0):
	print("Quotient:\tERROR (div by zero)")
else:
	print("Quotient:\t{}".format(float(nb1) / float(nb2)))
if (nb2 == 0):
	print("Remainder:\tERROR (modulo by zero)")
else:
	print("Remainder:\t{}".format(nb1 % nb2))
