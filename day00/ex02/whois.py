import sys

if len(sys.argv) != 2:
	print("ERROR")
	quit()
try:
	nb = int(sys.argv[1])
except:
	print("ERROR")
	quit()
else:
	if nb == 0:
		print("I'm Zero.")
	elif nb % 2:
		print("I'm Odd.")
	else:
		print("I'm Even.")
