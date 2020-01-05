# Base recipes
sandwich = {
	'ingredients': ["ham","bread","cheese","tomatoes"],
	'meal': "lunch",
	'prep_time': 10
}
cake = {
	'ingredients': ["flour","sugar","eggs"],
	'meal': "dessert",
	'prep_time': 60
}
salad = {
	'ingredients': ["avocado","arugula","tomatoes","spinach"],
	'meal': "lunch",
	'prep_time': 15
}

# Cookbook
cookbook = {
	'sandwich': sandwich,
	'cake': cake,
	'salad': salad
}

# Print functions
def print_recipe(cookbook, recipe):
	print("recipe for {}:".format(recipe))
	print("Ingredients list: {}".format(cookbook[recipe]['ingredients']))
	print("To be eaten for {}.".format(cookbook[recipe]['meal']))
	print("Takes {} minutes of cooking".format(cookbook[recipe]['prep_time']))

def print_cookbook(cookbook):
	for recipe in cookbook:
		print_recipe(cookbook, recipe)

def print_menu():
	print("Please select an option by typing the corresponding number:")
	print("1: Add a recipe")
	print("2: Delete a recipe")
	print("3: Print a recipe")
	print("4: Print the cookbook")
	print("5: Quit")

def print_menu_error():
	print("This option does not exist,", end = '')
	print("please type the corresponding number.")
	print("To exit, enter 5.")
	return 0

def get_choice(menu_choice):
	while (menu_choice == 0):
		try:
			menu_choice = int(input(>> ))
			if (menu_choice < 1 or menu_choice > 5)
				menu_choice = print_menu_error()
		except:
			menu_choice = print_menu_error()
	return menu_choice

def get_recipe(recipe):
	while (recipe == ""):
		try:
			recipe = raw_input(>> )
			if recipe not in cookbook.keys():
				recipe = ""
		except:
			recipe = ""
			print("This option does not exist,", end = '')
			print("please type the corresponding number.")
			print("To exit, enter 5.")
	return menu_choice

print_menu()
menu_choice = get_choice(0)
if (menu_choice == 3):
	recipe = get_recipe("")
	print_recipe(cookbook, recipe)
elif (menu_choice == 4):
	print_cookbook(cookbook)
elif (menu_choice == 5):
	quit()
