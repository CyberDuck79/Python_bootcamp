from typing import List

class Recipe:

	def __init__(self, name: str, cooking_lvl: int, cooking_time: int, ingredients: List[str], recipe_type: str, description = ""):
		if not name or not cooking_lvl or not cooking_time or not ingredients or not recipe_type:
			raise ValueError('Void value error')
		if recipe_type != "starter" and recipe_type != "lunch" and recipe_type != "dessert":
			raise ValueError('Recipe type not allowed, should be starter, lunch or dessert.')
		self.name = name
		self.cooking_lvl = cooking_lvl
		self.cooking_time = cooking_time
		self.ingredients = ingredients
		self.description = description
		self.recipe_type = recipe_type

	def __str__(self):
		"""Return the string to print with the recipe info"""
		txt = f"Recipe name : {self.name}\nCooking level : {self.cooking_lvl}\nTakes {self.cooking_time} minutes of cooking\n"
		txt += f"Ingredients : {self.ingredients}\nDescription : {self.description}\nTo be eaten for {self.recipe_type}"
		return txt