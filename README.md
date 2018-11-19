# Concoction :cocktail:
Generate a **Chef** program that outputs given string, as a means of _creative encryption_. :egg:

## What :grey_question:
This script will take a string and generate a program (`concoction.chef`) written in the [Chef](http://www.dangermouse.net/esoteric/chef.html) esoteric programming language.

Since Chef is a fairly obscure language that, to those that aren't familiar with it, doesn't really look like code, its use is suggested to be a creative way of encrypting a string.

The way to "decrypt" it is to use a [Chef interpreter](https://github.com/mpw96/perl-Acme-Chef) to run the generated program.

## How :question:
Generating:
* Get yourself [Python 3](https://www.python.org/downloads/)
* Run the script with a given string
* Check out the generated `.chef` file

Running Chef:
* Install a [Chef interpreter](https://github.com/mpw96/perl-Acme-Chef)
* Run the generated `.chef` file with the interpreter

## Running the Script :page_facing_up:
`concoction.py "Hello World"` (Generating)

`concoction.py -f my_file.txt` (Generating from file contents)

`concoction.py -o my_outputfile.txt "Hello World"` (Setting the output file name)

`chef concoction.chef` (Running Chef)

## Usage :information_source:
```
usage: concoction.py [-h] [-o OUTPUT] [-f] [-v] [-s] input

positional arguments:
    input                       string to convert to chef program

optional arguments:
    -h, --help                  show this help message and exit
    -o OUTPUT, --output OUTPUT  set filename for generated chef program, 
                                default is concoction.chef
    -f, --file                  use file as input
    -v, --verbose               allow verbose; the script will print out
                                what it's doing, default is False
    -s, --seeded                allow seeded randomness; the script will
                                use the given input string as a seed for
                                the randomization, default is False
```

## Note :exclamation:
The script currently supports a limited amount of characters, see [`ingredients.py`](https://github.com/Maxzilla60/Concoction/blob/master/ingredients.py).

Obviously, do **not** attempt to create and drink the generated concoctions! :worried:

## TODO :clipboard:
- [x] **More creative names for [`ingredients.py`](https://github.com/Maxzilla60/Concoction/blob/master/ingredients.py)!**
- [x] Random recipe title
- [x] Also get dry ingredients into the mix!
- [x] Support files as input
- [ ] Remove one-to-one relationship between ASCII character and ingredient name
- [ ] Unit tests
- [ ] Fix web version
