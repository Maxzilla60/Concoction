from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse
import argparse
import concoction

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

            self.wfile.write(concoction.Concoction().process(
                map(lambda x: x, str(query_components["recipe"]))))


def run(server_class=HTTPServer, handler_class=WebServer, port=80, verbose=False):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    if verbose:
        print("Starting httpd...")
    httpd.serve_forever()


def parse_args():
    # Parsing args
    parser = argparse.ArgumentParser(description="Concoction.py - Generate a Chef program that outputs given string, as a means of creative encryption.", epilog="https://github.com/Maxzilla60/Concoction")
    parser.add_argument("-f", "--file", action="store_true", help="use file as input")
    parser.add_argument("input", metavar="input", type=str, help="string to convert to chef program")
    parser.add_argument("-o", "--output", action="store", type=str, help="set filename for generated chef program, default is concoction.chef", default="concoction.chef")
    parser.add_argument("-v", "--verbose", action="store_true", help="allow verbose; the script will print out what it's doing")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    my_concoction = concoction.Concoction(args.verbose)
    my_output_file = args.output
    my_input_text = args.input
    if args.file:
        my_input_text = my_concoction.read_file(args.file)
    my_concoction.write_file(my_output_file, my_concoction.process(my_input_text))
