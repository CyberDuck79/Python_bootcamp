import string

def text_analyzer(text = ""):
	"""This function counts the number of upper characters, lower characters, punctuation and spaces in a given text."""
	while text == "":
		text = input("What is the text to analyse?\n>> ")
	print(f"The text contains {len(text)} characters:")
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
	print(f"- {upper_letters} upper letters")
	print(f"- {lower_letters} lower letters")
	print(f"- {punctuation_marks} punctuation marks")
	print(f"- {spaces} spaces")