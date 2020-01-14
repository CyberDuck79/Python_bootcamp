from random import shuffle

# function prototype
def generator(text: str, sep: str=" ", option: str=""):
	'''Option is an optional arg, sep is mandatory'''
	options = ["shuffle", "unique", "ordered"]
	if not isinstance(text, str):
		raise TypeError("type error")
	if not text:
		raise ValueError("test is void")
	if option and option not in options:
		raise ValueError("option invalid")
	split = text.split(sep)
	if option == options[0]:
		shuffle(split)
	elif option == options[1]:
		split = list(dict.fromkeys(split))
	elif option == options[2]:
		split = sorted(split, key=str.casefold)
		print(split)
	for word in split:
		yield word

text = "Le Lorem Ipsum est simplement du faux texte."
for word in generator(text, sep=" ", option="ordered"):
	print(word)
