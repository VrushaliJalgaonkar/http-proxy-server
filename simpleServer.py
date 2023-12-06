import socketserver
import http.server
import urllib.request
import shutil
import tempfile

PORT = 9097

class MyProxy(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
    	url=self.path[1:]
    	self.send_response(200)
    	self.end_headers()
    	req = urllib.request.urlopen(url)
    	self.copyfile(req, self.wfile)
server_address = ('', PORT)
httpd = http.server.HTTPServer(server_address, MyProxy)
print ("Now serving at",str(PORT))
httpd.serve_forever()
