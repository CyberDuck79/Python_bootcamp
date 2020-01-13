import sys

if len(sys.argv) != 3:
	print("ERROR")
	quit()
try:
	nb = int(sys.argv[1])
	print("ERROR")
	quit()
except ValueError:
	arg_str = sys.argv[1]
try:
	nb = int(sys.argv[2])
except ValueError:
	print("ERROR")
	quit()
return_lst = []
word_lst = arg_str.split()
for word in word_lst:
	if len(word) > nb:
		return_lst.append(word)
print(return_lst)