import argparse, concoction

def parse_args():
    # Parsing args
    parser = argparse.ArgumentParser(description="Concoction.py - Generate a Chef program that outputs given string, as a means of creative encryption.", epilog="https://github.com/Maxzilla60/Concoction")
    parser.add_argument("input", metavar="input", type=str, help="string to convert to chef program")
    parser.add_argument("-o", "--output", action="store", type=str, help="set filename for generated chef program, default is concoction.chef", default="concoction.chef")
    parser.add_argument("-f", "--file", action="store_true", help="use file as input")
    parser.add_argument("-v", "--verbose", action="store_true", help="allow verbose; the script will print out what it's doing, default is False")
    parser.add_argument("-s", "--seeded", action="store_true", help="allow seeded randomness; the script will use the given input string as a seed for the randomization, default is False")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    my_input_text = args.input
    my_concoction = concoction.Concoction(my_input_text, verbose=args.verbose, seeded=args.seeded)
    my_output_file = args.output
    if args.file:
        my_input_text = my_concoction.read_file(args.file)
    my_concoction.write_file(my_output_file, my_concoction.generate_chefrecipe())
