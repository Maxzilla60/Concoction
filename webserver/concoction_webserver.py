import ..concoction
import argparse
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse

class WebServer(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        if self.path[:9] != "/?recipe=":
            self.wfile.write("You must give recipe parameter")
        else:
            query_components = parse.parse_qs(parse(self.path).query)

            if "recipe" not in query_components:
                self.wfile.write("You must give recipe parameter")

            self.wfile.write(concoction.Concoction(
                map(lambda x: x, str(query_components["recipe"]))
            ).generate_chefrecipe())


def run(server_class=HTTPServer, handler_class=WebServer, port=80, verbose=False):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    if verbose:
        print("Starting httpd...")
    httpd.serve_forever()


def parse_args():
    # Parsing args
    parser = argparse.ArgumentParser(description="Concoction.py [Webserver version] - Generate a Chef program that outputs given string, as a means of creative encryption.", epilog="https://github.com/Maxzilla60/Concoction")
    parser.add_argument("-p", "--port", type=int, action="store", help="set port, default is 80", default=80)
    parser.add_argument("-v", "--verbose", action="store_true", help="allow verbose; the script will print out what it's doing, default is False")
    return parser.parse_args()


args = parse_args()
run(port=args.port, verbose=args.verbose)