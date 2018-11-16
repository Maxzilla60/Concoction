import random, sys
from ingredients import ingredients_dictionary


class Concoction:
    def __init__(self, input_string, verbose=False, seeded=False, from_file=False):
        self.ingredients = {}
        self.verbose = verbose
        self.seeded = seeded
        if from_file:
            self.input_string = self.get_input_fromfile(input_string)
        else:
            self.input_string = input_string

    def get_input_fromfile(self, input_filename):
        if self.verbose:
            print("Reading input file...")
        try:
            return ''.join(open(input_filename, "r").readlines())
        except IOError:
            print("Could not read file: " + input_filename)
            sys.exit()

    def generate_chefrecipe(self):
        self.set_seed()
        self.get_ingredients()
        output = self.get_recipetitle()
        output += ".\n\n"
        output += "Ingredients.\n"
        output += self.generate_ingredients() + "\n"
        output += "Method.\n"
        output += self.generate_method() + "\n"
        output += "Serves 1."
        self.reset_seed()
        return output

    def get_ingredients(self):
        # Parse input and make a list of used ingredients:
        for c in self.input_string:
            self.ingredients[c] = ingredients_dictionary[c]

    def get_recipetitle(self):
        if self.verbose:
            print("Naming concoction...")
        # Easter Egg: when the input is just whitespace:
        if self.input_string.isspace():
            return "Bowl of Nothing"
        # Easter Egg: when the input contains one or multiples of one ingredient:
        if self.input_string == len(self.input_string) * self.input_string[0]:
            return self.oneingredient_title()
        title_prefixes = ["Awful","Barf","Horrible","Magic","Secret","Strange"]
        title_suffixes = ["Cocktail","Concoction","Drink","Mixture","Potion","Recipe"]
        title = "" + random.choice(title_prefixes) + " " + random.choice(title_suffixes)
        return title

    def generate_ingredients(self):
        if self.verbose:
            print("Writing ingredients...")
        ingredients_string = "" # string to return
        measures = ["ml", "l", "dashes"]  # different measures to randomize
        items = list(self.ingredients.items())  # Convert ingredients to list
        random.shuffle(items)  # Shuffle the list
        # Go through the ingredients and write out respective ingredient items:
        for key, value in items:
            # "[ASCII value] [random measure] [ingredient name]"
            ingredients_string += str(ord(key)) + " " + random.choice(measures) + " " + value + "\n"
        return ingredients_string

    def generate_method(self):
        if self.verbose:
            print("Writing method...")
        method_string = "" # string to return
        reversed_input_string = self.input_string[::-1]  # Reverse input
        # Go through the characters of input text and write out respective methods:
        for c in reversed_input_string:
            method_string += "Put " + self.ingredients[c] + " into mixing bowl.\n"
        method_string += "Pour contents of the mixing bowl into the baking dish.\n"
        return method_string

    def oneingredient_title(self):
        title = "Bowl of"
        ingredient_name = ingredients_dictionary[self.input_string[0]].split()
        for word in ingredient_name:
            title += " " + word.capitalize()
        return title

    def set_seed(self):
        if self.seeded:
            random.seed(self.input_string)
    
    def reset_seed(self):
        random.seed()
