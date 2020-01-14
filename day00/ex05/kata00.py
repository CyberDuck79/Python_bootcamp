t = (19,42,21)
print("the 3 numbers are: ", end ='')
for elem in t[:-1]:
	print(f"{elem}, ", end = '')
print(f"{t[-1]}")