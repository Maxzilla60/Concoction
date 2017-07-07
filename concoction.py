import sys, shutil, random
# import dictionary
from ingredients import ingredients_dictionary

# Get input (arguments):
if len(sys.argv) < 2:
	print("Please provide a string as argument.")
	exit()
uhoh = len(sys.argv) > 2
input = sys.argv[1]

# Create file:
print("Creating file concoction.chef...")
recipe = open("concoction.chef", "w+")
recipe.write("Strange Concoction.\n\n")

# Ingredients:
print("Parsing input...")
recipe.write("Ingredients.\n")
ingredients = {} # list of used ingredients
# Parse input and make a list of used ingredients:
for c in input:
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
input = input[::-1] # reverse input
for c in input:
	recipe.write("Put " + ingredients[c] + " into mixing bowl. ")
#recipe.write("\nPour contents of the mixing bowl into the baking dish. Refrigerate for 1 hours.")
recipe.write("\nPour contents of the mixing bowl into the baking dish.\n\nServes 1.")

recipe.close()
print("Done!")
if uhoh:
	print("NOTICE: You've provided more than one argument, maybe you forgot to add around your given string?")
