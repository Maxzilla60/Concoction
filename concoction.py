import sys
import random
from ingredients import ingredients_dictionary

class Concoction:
    def __init__(self, verbose=False):
        self.verbose = verbose

    def read_file(self, file_arg):
        if self.verbose:
            print("Reading input file...")
        try:
            return open(file_arg, "r").readline().strip()
        except IOError:
            print("Could not read file: " + file_arg)
            sys.exit()

    def write_file(self, file_arg, file_content):
        if self.verbose:
            print("Writing out file...")
        try:
            recipe = open(file_arg, "w+")
            recipe.write(file_content)
            recipe.close()
        except IOError:
            print("Could not write file: " + file_arg)
            sys.exit()

        if self.verbose:
            print("Done!")

    def generate_chefrecipe(self, input_text):
        self.set_seed(input_text)
        ingredients = self.get_ingredients(input_text)
        output = self.get_recipetitle(input_text)
        output += ".\n\n"
        output += "Ingredients.\n"
        output += self.generate_ingredients(input_text, ingredients) + "\n"
        output += "Method.\n"
        output += self.generate_method(input_text, ingredients) + "\n"
        output += "Pour contents of the mixing bowl into the baking dish.\n\n"
        output += "Serves 1."
        self.reset_seed()
        return output

    def get_ingredients(self, input_text):
        ingredients = {} # list to return
        # Parse input and make a list of used ingredients:
        for c in input_text:
            ingredients[c] = ingredients_dictionary[c]
        return ingredients

    def get_recipetitle(self, input_text=None):
        if self.verbose:
            print("Naming concoction...")
        title_prefixes = [
            "Awful",
            "Barf",
            "Horrible",
            "Magic",
            "Secret",
            "Strange",
        ]
        title_suffixes = [
            "Cocktail",
            "Concoction",
            "Drink",
            "Mixture",
            "Potion",
            "Recipe",
        ]
        title = "" + random.choice(title_prefixes) + " " + random.choice(title_suffixes)
        return title

    def generate_ingredients(self, input_text, ingredients):
        if self.verbose:
            print("Writing ingredients...")
        ingredients_string = "" # string to return
        measures = ["ml", "l", "dashes"]  # different measures to randomize
        items = list(ingredients.items())  # Convert ingredients to list
        random.shuffle(items)  # Shuffle the list
        # Go through the ingredients and write out respective ingredient items:
        for key, value in items:
            # "[ASCII value] [random measure] [ingredient name]"
            ingredients_string += str(ord(key)) + " " + random.choice(measures) + " " + value + "\n"
        return ingredients_string

    def generate_method(self, input_text, ingredients):
        if self.verbose:
            print("Writing method...")
        method_string = "" # string to return
        input_text = input_text[::-1]  # Reverse input
        # Go through the characters of input text and write out respective methods:
        for c in input_text:
            method_string += "Put " + ingredients[c] + " into mixing bowl.\n"
        return method_string

    def set_seed(self, input_text):
        random.seed(input_text)
    
    def reset_seed(self):
        random.seed()