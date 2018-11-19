## Webserver :globe_with_meridians:

:construction: **Currently not working** :construction:

### Usage :information_source:
```
usage: concoction_webserver.py [-h] [-p PORT] [-v]

optional arguments:
  -h, --help            		show this help message and exit
  -p PORT, --port PORT  		set port, default is 80
  -v, --verbose         		allow verbose; the script will print out
  								what it's doing
```

### Docker :whale:
Just clone, cd in it and build it : `docker build -t concoction .`

You can use another name instead of `concoction`.

And just run it : `docker run -p "80:8888" -ti concoction`.

If all is ok, just [go here](http://localhost:8888).
