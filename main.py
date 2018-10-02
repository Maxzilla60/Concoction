from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from urlparse import urlparse, parse_qs
import argparse
import concoction


class WebServer(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        if self.path[:9] != "/?recipe=":
            self.wfile.write("You must give recipe parameter")
        else:
            query_components = parse_qs(urlparse(self.path).query)

            if "recipe" not in query_components:
                self.wfile.write("You must give recipe parameter")

            self.wfile.write(concoction.Concoction().process(map(lambda x: x, str(query_components["recipe"]))))


def run(server_class=HTTPServer, handler_class=WebServer, port=80, verbose=False):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    if verbose:
        print 'Starting httpd...'
    httpd.serve_forever()


def parse_args():
    # Parsing args
    parser = argparse.ArgumentParser(description="Generate a Chef program")
    main_group = parser.add_mutually_exclusive_group()
    group_file = main_group.add_argument_group()
    group = group_file.add_mutually_exclusive_group()
    group.add_argument("-s", "--string", action="store", type=str, help="Set string as input", default="")
    group.add_argument("-f", "--file", action="store", type=str, help="Set file as input")
    group_file.add_argument("-o", "--out", action="store", type=str, help="Set file as output")
    main_group.add_argument("-p", "--port", action="store", type=int, help="Start as web server", default=-1)
    parser.add_argument("-v", "--verbose", action="store_true", help="Allow verbose")
    return parser.parse_args()


if __name__ == "__main__":

    args = parse_args()

    if args.port != -1:
        run(port=args.port,verbose=args.verbose)
    else:

        my_concoction = concoction.Concoction(args.verbose)

        my_output_file = "concoction.chef"
        if args.out is not None:
            my_output_file = args.out

        my_input_text = ""
        if args.string is not None and len(args.string) != 0:
            my_input_text = args.string
        else:
            if args.file is not None:
                my_input_text = my_concoction.read_file(args.file)

        my_concoction.write_file(my_output_file,my_concoction.process(my_input_text))
