import string

def text_analyzer(text = ""):
	"""This function counts the number of upper characters, lower characters,
punctuation and spaces in a given text."""
	while text == "":
		text = raw_input("What is the text to analyse?\n>> ")
	print("The text contains {} characters:".format(len(text)))
	upper_letters = 0
	lower_letters = 0
	punctuation_marks = 0
	spaces = 0
	for letter in text:
		if letter.isupper():
			upper_letters += 1
		elif letter.islower():
			lower_letters += 1
		elif letter.isspace():
			spaces += 1
		elif letter in string.punctuation:
			punctuation_marks += 1
	print("- {} upper letters".format(upper_letters))
	print("- {} lower letters".format(lower_letters))
	print("- {} punctuation marks".format(punctuation_marks))
	print("- {} spaces".format(spaces))