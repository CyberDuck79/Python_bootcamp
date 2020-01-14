from datetime import datetime
from typing import List
from recipe import Recipe

class Book:

	def __init__(self, name: str):
		if not name:
			raise ValueError('Void name error')
		self.name = str(name)
		self.creation_date = datetime.now().strftime("%D %T")
		self.last_update = datetime.now().strftime("%D %T")
		self.recipes_list = {
			'starter': [],
			'lunch': [],
			'dessert': []
		}

	def get_recipe_by_name(self, name: str):
		"""Print a recipe with the name `name` and return the instance"""
		if not name:
			raise ValueError('Void name error')
		for key in self.recipes_list:
			for recipe in self.recipes_list[key]:
				if recipe.name == name:
					print(recipe)
					return
		raise NameError('recipe do not exist in the book.')

	def get_recipes_by_types(self, recipe_type: str):
		"""Get all recipe names for a given recipe_type """
		if not recipe_type:
			raise ValueError('Void recipe_type error')
		if recipe_type != "starter" and recipe_type != "lunch" and recipe_type != "dessert":
			raise ValueError('Recipe type not allowed, should be starter, lunch or dessert.')
		for recipe in self.recipes_list[recipe_type]:
			print(recipe.name)
		pass

	def add_recipe(self, recipe: Recipe):
		"""Add a recipe to the book and update last_update"""
		if not isinstance(recipe, Recipe):
			raise TypeError('Non recipe input')
		if not recipe:
			raise ValueError('Void recipe object error')
		recipe_type = recipe.recipe_type
		if recipe_type != "starter" and recipe_type != "lunch" and recipe_type != "dessert":
			raise ValueError('Recipe type not allowed, should be starter, lunch or dessert.')
		self.recipes_list[recipe_type].append(recipe)
		pass