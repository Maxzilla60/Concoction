import sys
import random
import argparse

# import dictionary
from ingredients import ingredients_dictionary

# Parsing args
parser = argparse.ArgumentParser(description="Generate a Chef program")
group = parser.add_mutually_exclusive_group()
group.add_argument("-s", "--string", action="store", type=str, help="Set string as input", default="")
group.add_argument("-f", "--file", action="store", type=str, help="Set file as input")
parser.add_argument("-o", "--out", action="store", type=str, help="Set file as output")
args = parser.parse_args()

# Analyse args
output = "concoction.chef"
if args.out is not None:
	output = args.out

inputText = ""
if args.string is not None and len(args.string) != 0 :
	inputText = args.string
else:
	if args.file is not None:
		try:
			fileInArg = open(args.file, "r")
			inputText = fileInArg.readline().strip()
		except IOError:
			print("Could not read file: " + args.file)
			sys.exit()


# Create file:
print("Creating file concoction.chef...")
try:
	recipe = open(output, "w+")
except IOError:
	print("Could not write file: " + output)
	sys.exit()
recipe.write("Strange Concoction.\n\n")

# Ingredients:
print("Parsing input...")
recipe.write("Ingredients.\n")
ingredients = {} # list of used ingredients
# Parse input and make a list of used ingredients:

for c in inputText:
	ingredients[c] = ingredients_dictionary[c]

print("Writing ingredients...")
measures = ["ml", "l", "dashes"] # different measures to randomize
items = list(ingredients.items()) # convert ingredients to list
random.shuffle(items) # shuffle this list
# Go through the ingredients and print 'em to the file:
for key, value in items:
	# "[ASCII value] [random measure] [ingredient name]"
	recipe.write("" + str(ord(key)) + " " + random.choice(measures) + " " + value + "\n")
recipe.write("\n")

# Method:
print("Writing method...")
recipe.write("Method.\n")
inputText = inputText[::-1] # Reverse input
for c in inputText:
	recipe.write("Put " + ingredients[c] + " into mixing bowl.\n")
recipe.write("\nPour contents of the mixing bowl into the baking dish.\n\nServes 1.")

recipe.close()
print("Done!")
