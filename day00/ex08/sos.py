import sys

morse_alphabet = {
	'A': ".-",
	'B': "-...",
	'C': "-.-.",
	'D': "-..",
	'E': ".",
	'F': "..-.",
	'G': "--.",
	'H': "....",
	'I': "..",
	'J': ".---",
	'K': "-.-",
	'L': ".-..",
	'M': "--",
	'N': "-.",
	'O': "---",
	'P': ".--.",
	'Q': "--.-",
	'R': ".-.",
	'S': "...",
	'T': "-",
	'U': "..-",
	'V': "...-",
	'W': ".--",
	'X': "-..-",
	'Y': "-.--",
	'Z': "--..",
	'0': "-----",
	'1': ".----",
	'2': "..---",
	'3': "...--",
	'4': "....-",
	'5': ".....",
	'6': "-....",
	'7': "--...",
	'8': "---..",
	'9': "----."
}

def check_input(string):
	for letter in string:
		if not letter.isalnum() and letter != ' ':
			print("ERROR")
			quit()

def convert_input(string):
	for letter in string:
		if letter == ' ':
			print("/ ", end='')
		else:
			print(morse_alphabet[letter], end=' ')

if (len(sys.argv) == 1):
	quit()
arg_lst = sys.argv[1:]
for arg in arg_lst:
	check_input(arg)
count = 0
while count < len(arg_lst) - 1:
	convert_input(arg_lst[count].upper())
	print("/ ", end='')
	count += 1
convert_input(arg_lst[count].upper())
print()
