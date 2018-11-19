import argparse, random, sys, logging
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
        logging.info("Reading input file...")
        try:
            return open(input_filename, "r").read()
        except IOError:
            logging.error("Could not read file: " + input_filename)
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
        measures = ["ml", "l", "dashes", "g", "kg", "pinches", "cups", "teaspoons", "tablespoons"]
        # Parse input and make a list of used ingredients:
        for c in self.input_string:
            self.ingredients[c] = { 'name': ingredients_dictionary[c], 'measure': random.choice(measures) }

    def get_recipetitle(self):
        logging.info("Naming concoction...")
        # Easter Egg: when the input is just whitespace:
        if self.input_string.isspace():
            return "Bowl of Nothing"
        # Easter Egg: when the input contains one or multiples of one ingredient:
        if self.input_string == len(self.input_string) * self.input_string[0]:
            return self.oneingredient_title()
        title_prefixes = ["Awful","Barf","Horrible","Magic","Secret","Strange"]
        title_suffixes = ["Cocktail","Concoction","Drink","Mixture","Potion","Recipe"]
        return "" + random.choice(title_prefixes) + " " + random.choice(title_suffixes)

    def generate_ingredients(self):
        logging.info("Writing ingredients...")
        ingredients_string = "" # string to return
        items = list(self.ingredients.items())
        random.shuffle(items)
        # Go through the ingredients and write out respective ingredient items:
        for key, value in items:
            # "[ASCII value] [random measure] [ingredient name]"
            ingredients_string += str(ord(key)) + " " + value['measure'] + " " + value['name'] + "\n"
        return ingredients_string

    def generate_method(self):
        logging.info("Writing method...")
        method_string = ""
        reversed_input_string = self.input_string[::-1]  # Reverse input
        # Go through the characters of input text and write out respective methods:
        for c in reversed_input_string:
            method_string += "Put " + self.ingredients[c]['name'] + " into mixing bowl.\n"
        method_string += "Liquefy contents of the mixing bowl.\n" # Liquefy in case there are dry ingredients
        method_string += "Pour contents of the mixing bowl into the baking dish.\n"
        return method_string

    def oneingredient_title(self):
        # Generate title for a recipe that uses only one ingredient:
        title = "Bowl of"
        ingredient_name = ingredients_dictionary[self.input_string[0]].split()
        for word in ingredient_name:
            title += " " + word.capitalize()
        return title

    def set_seed(self):
        # Use input text as seed for randomization
        if self.seeded:
            random.seed(self.input_string)
    
    def reset_seed(self):
        random.seed()


def parse_args():
    parser = argparse.ArgumentParser(description="Concoction.py - Generate a Chef program that outputs given string, as a means of creative encryption.", epilog="https://github.com/Maxzilla60/Concoction")
    parser.add_argument("input", metavar="input", type=str, help="string to convert to chef program")
    parser.add_argument("-o", "--output", action="store", type=str, help="set filename for generated chef program, default is concoction.chef", default="concoction.chef")
    parser.add_argument("-f", "--file", action="store_true", help="use file as input")
    parser.add_argument("-v", "--verbose", action="store_true", help="allow verbose; the script will print out what it's doing, default is False")
    parser.add_argument("-s", "--seeded", action="store_true", help="allow seeded randomness; the script will use the given input string as a seed for the randomization, default is False")
    return parser.parse_args()

def configureLogging(verbose=False):
    if verbose:
        logging.basicConfig(format="%(message)s", level=logging.INFO)
    else:
        logging.basicConfig(format="%(message)s")

def write_file(output_filename, file_content, verbose=False):
    if verbose:
        logging.info("Writing out file...")
    try:
        recipe = open(output_filename, "w+")
        recipe.write(file_content)
        recipe.close()
    except IOError:
        logging.error("Could not write file: " + output_filename)
        sys.exit()
    if verbose:
        logging.info("Done, bon appetit!")

args = parse_args()
configureLogging(args.verbose)
my_concoction = Concoction(args.input, verbose=args.verbose, seeded=args.seeded, from_file=args.file)
write_file(args.output, my_concoction.generate_chefrecipe(), verbose=args.verbose)
print(args.output)
