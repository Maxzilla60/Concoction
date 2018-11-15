import sys
import random

# import dictionary
from ingredients import ingredients_dictionary

class Concoction:
    def __init__(self, verbose=False):
        self.verbose = verbose

    def read_file(self, file_arg):
        if self.verbose:
            print("Read input file")
        try:
            return open(file_arg, "r").readline().strip()
        except IOError:
            print("Could not read file: " + file_arg)
            sys.exit()

    def write_file(self, file_arg, file_content):
        if self.verbose:
            print("Write out file")
        try:
            recipe = open(file_arg, "w+")
            recipe.write(file_content)
            recipe.close()
        except IOError:
            print("Could not write file: " + file_arg)
            sys.exit()

        if self.verbose:
            print("Done!")

    def process(self, input_text):
        output = "Strange Concoction.\n\n"
        output += "Ingredients.\n"

        ingredients = {} # list of used ingredients
        # Parse input and make a list of used ingredients:

        for c in input_text:
            ingredients[c] = ingredients_dictionary[c]

        if self.verbose:
            print("Writing ingredients...")

        measures = ["ml", "l", "dashes"]  # different measures to randomize
        items = list(ingredients.items())  # convert ingredients to list
        random.shuffle(items)  # shuffle this list
        # Go through the ingredients and print 'em to the file:
        for key, value in items:
            # "[ASCII value] [random measure] [ingredient name]"
            output += str(ord(key)) + " " + random.choice(measures) + " " + value + "\n"
        output += "\n"

        # Method:
        if self.verbose:
            print("Writing method...")
        output += "Method.\n"

        input_text = input_text[::-1]  # Reverse input
        for c in input_text:
            output += "Put " + ingredients[c] + " into mixing bowl.\n"
        output += "\nPour contents of the mixing bowl into the baking dish.\n\nServes 1."
        return output
