# Concoction :cocktail:
Generate a **Chef** program that outputs given string, as a means of _creative encryption_. :egg:

## What:question:
This script will take a string and generate a program (`concoction.chef`) written in the [Chef](http://www.dangermouse.net/esoteric/chef.html) esoteric programming language.

Since Chef is a fairly obscure language that, to those that aren't familiar with it, doesn't really look like code, its use is suggested to be a creative way of encrypting a string.

The way to "decrypt" it is to use a [Chef interpreter](https://github.com/mpw96/perl-Acme-Chef) to run the generated program... or you could try and figure out the program on your own, if you want. :sweat_smile:

## How:question:
Generating:
* Get yourself [Python 3](https://www.python.org/downloads/)
* Run the script (the script must be run with a given string)
* Check out the generated Chef file (`concoction.chef`)

Running Chef:
* Install a [Chef interpreter](https://github.com/mpw96/perl-Acme-Chef)
* Run `concoction.chef` with the interpreter

## Running as executable :page_facing_up:
`main.py -s "Hello World"` (Generating)

`main.py -f "file name"` (Generating)

`chef concoction.chef` (Running Chef)

## Running as webserver :page_facing_up:

Just launch has that :

`main.py -p PORT` 

## Running as webserver in Docker :page_facing_up:

Just clone, cd in it and build it : `docker build -t concoction .`

You can use another name instead of `concoction`.

And just run it : `docker run -p "80:8888" -ti concoction`.

If all is ok, just [go here](http://localhost:8888).

## Note:exclamation:
The script supports a limited amount of characters, see [`ingredients.py`](https://github.com/Maxzilla60/Concoction/blob/master/ingredients.py).

Obviously, do **not** attempt to create and drink the generated concoctions! :worried:

### TODO :clipboard:
- [ ] **More creative names for [`ingredients.py`](https://github.com/Maxzilla60/Concoction/blob/master/ingredients.py)!**
- [ ] Also get dry ingredients into the mix!
- [x] Support files as input/output
- [x] Web version?
