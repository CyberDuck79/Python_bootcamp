from random import randint

print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!\n")

number = randint(1, 99)
answer = 0
attempt = 0
while (answer != number):
	try:
		print("What's your guess between 1 and 99?")
		text = input(">> ")
		if (text == "exit"):
			print("Goodbye!")
			quit()
		answer = int(text)
		attempt += 1
		if (answer > number):
			print("Too high!")
		elif (answer < number):
			print("Too low!")
	except ValueError:
		print("That's not a number.")
		answer = 0
if (number == 42):
	print("The answer to the ultimate question of life, the universe and everything is 42.")
if (attempt == 1):
	print("Congratulations! You got it on your first try!")
else:
	print("Congratulations, you've got it!")
	print("You won in {} attempts!".format(attempt))
