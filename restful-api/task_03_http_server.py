#!/usr/bin/python3
'''
This module provides a simple HTTP server capable of using JSON and have
some custom API endpoints.
'''
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleHandler(BaseHTTPRequestHandler):
    '''
    This class is inherited from BaseHTTPRequestHandler.
    It defines a simple do_GET method to implement some endpoints for a
    basic API.
    '''
    def do_GET(self):
        '''
        This is the method to handle simple endpoints with a simple HTTP
        server. It contains 3 paths and handle others with error code 404.
        '''
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            dataset = {"name": "John", "age": 30, "city": "New York"}
            json_datas = json.dumps(dataset)
            json_bytes = json_datas.encode('utf-8')
            self.wfile.write(json_bytes)

        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run(server_class=HTTPServer, handler_class=SimpleHandler, port=8000):
    '''
    This is the method that runs the server in localhost.
    Args:
        server_class: The HTTP server class to use, defaulted to HTTPServer
        handler_class: The HTTP request handler, defaulted to SimpleHandler
        port: The port on which the server is listening, defaulted to 8000
    '''
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Serveur en écoute sur http://localhost/{port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
