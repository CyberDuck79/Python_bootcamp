from book import Book
from recipe import Recipe

cookbook = Book("cookbook")
recipe1 = Recipe("cake", 2, 60, ["eggs","tet"], "dessert")
# les self ne se mettent pas automatiquement ????
cookbook.add_recipe("plop")
cookbook.get_recipes_by_types("dessert")
cookbook.get_recipe_by_name("cake")