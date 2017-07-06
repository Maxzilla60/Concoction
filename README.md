# Concoction :cocktail:
Generate a **Chef** program that outputs given string, as a means of creative _encryption_. :egg:

## What:question:
This script will take a string and generate a program (`concoction.chef`) written in the [Chef](http://www.dangermouse.net/esoteric/chef.html) esoteric programming language.

Its use is suggested to be a creative way of encrypting a string. The way to "decrypt" it is to use a [Chef interpreter](https://github.com/mpw96/perl-Acme-Chef) to run the generated program... or you could try and figure out the program on your own, if you want. :sweat_smile:

## How:question:
Generating:
* Get yourself [Python 3](https://www.python.org/downloads/)
* Run the script (the script must be run with a given string)
* Check out the generated Chef file (`concoction.chef`)

Running Chef:
* Install a [Chef interpreter](https://github.com/mpw96/perl-Acme-Chef)
* Run `concoction.chef` with the interpreter

## Running :page_facing_up:
`concoction.py "Hello World"` (Generating)

`chef concoction.chef` (Running Chef)

## Note:exclamation:
The script supports a limited amount of characters, see [`ingredients.py`](https://github.com/Maxzilla60/Concoction/blob/master/ingredients.py).

Obviously, do **not** attempt to create and drink the generated concoctions! :worried:

### TODO :clipboard:
- [ ] **More creative names for [`ingredients.py`](https://github.com/Maxzilla60/Concoction/blob/master/ingredients.py)!**
- [ ] Support files as input?
- [ ] Web version?
