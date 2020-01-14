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
def print_recipe(recipe):
	print(f"\nrecipe for {recipe}:")
	print(f"Ingredients list: {cookbook[recipe]['ingredients']}")
	print(f"To be eaten for {cookbook[recipe]['meal']}.")
	print(f"Takes {cookbook[recipe]['prep_time']} minutes of cooking")

def print_cookbook():
	for recipe in cookbook:
		print_recipe(recipe)

def print_menu():
	print("\nPlease select an option by typing the corresponding number:")
	print("1: Add a recipe")
	print("2: Delete a recipe")
	print("3: Print a recipe")
	print("4: Print the cookbook")
	print("5: Quit")

# Print errors functions
def print_menu_error():
	print("This option does not exist, ", end = '')
	print("please type the corresponding number.")
	print("To exit, enter 5.")

def print_recipe_error():
	print("This option does not exist, ", end = '')
	print("please type a corresponding name.")
	print("To return to the menu type cancel.")

def print_name_error():
	print("Name cannot be blank, ", end = '')
	print("to return to the menu type cancel.")

def print_time_error():
	print("Error type, enter a number.")
	print("to return to the menu type 0.")
	return 0

# Inputs functions
def get_choice():
	menu_choice = 0
	while (menu_choice == 0):
		try:
			menu_choice = int(input(">> "))
			if (menu_choice < 1 or menu_choice > 5):
				menu_choice = 0
				print_menu_error()
		except ValueError:
			menu_choice = 0
			print_menu_error()
	return menu_choice

def get_recipe():
	recipe = ""
	while (recipe == ""):
		print("Please enter a recipe name :")
		recipe = input(">> ")
		if recipe == "cancel":
			return recipe
		if recipe not in cookbook.keys():
			recipe = ""
			print_recipe_error()
	return recipe

def get_name():
	name = ""
	while (name == ""):
		print("Please enter a name :")
		name = input(">> ")
		if name == "cancel":
			return name
		if name == "":
			print_name_error()
	return name

def	get_time():
	time = 0
	while (time == 0):
		try:
			print("Please enter time in minutes :")
			time = int(input(">> "))
			if (time == 0):
				return time
		except ValueError:
			time = 0
			print_time_error()
	return time

def get_ingredients():
	name = ""
	ingredients = []
	print("\nIngredients")
	print("type end to close the ingredients list")
	while (name != "end" and name != "cancel"):
		name = get_name()
		if name == "end":
			if len(ingredients) != 0:
				return ingredients
			else:
				print("no ingredient in the list.")
				name = ""
		if name != "" and name not in ingredients:
			ingredients.append(name)
		else:
			print("ingredient already in list.")
	if name == "cancel":
		ingredients = []
	return ingredients

# Modifications functions
def del_recipe(recipe):
	del cookbook[recipe]

def add_recipe():
	recipe = {}
	print("\nRecipe name")
	name = get_name()
	if name == "cancel":
		return
	ingredients = get_ingredients()
	if (len(ingredients) == 0):
		return
	recipe['ingredients'] = ingredients
	print("Type of meal")
	meal = get_name()
	if meal == "cancel":
		return
	recipe['meal'] = meal
	prep_time = get_time()
	if prep_time == 0:
		return
	recipe['prep_time'] = prep_time
	cookbook[name] = recipe

#
while (1):
	print_menu()
	menu_choice = get_choice()
	if (menu_choice == 1):
		add_recipe()
	elif (menu_choice == 2):
		recipe = get_recipe()
		if recipe != "cancel":
			del_recipe(recipe)
	elif (menu_choice == 3):
		recipe = get_recipe()
		if recipe != "cancel":
			print_recipe(recipe)
	elif (menu_choice == 4):
		print_cookbook()
	elif (menu_choice == 5):
		quit()
