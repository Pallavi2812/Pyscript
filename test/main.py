from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os
 
def my_function():
    return "Hello from Python!"
 
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('index.html', 'rb') as file:
                self.wfile.write(file.read())
        elif self.path == '/call_function':
            result = my_function()
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = json.dumps({"result": result})
            self.wfile.write(response.encode())
        else:
            self.send_response(404)
            self.end_headers()
 
def run(server_class=HTTPServer, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, RequestHandler)
    print(f'Serving on port {port}...')
    httpd.serve_forever()
 
if __name__ == '__main__':
    run()
