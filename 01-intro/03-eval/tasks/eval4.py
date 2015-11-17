#!/usr/bin/python -u
# task4.py
from BaseHTTPServer import HTTPServer,BaseHTTPRequestHandler
from SocketServer import ForkingMixIn
from cgi import escape
from os import path
from sys import stdin,stdout
import traceback

# Make a simple HTML page from the given content
def makepage(title, content, headers=""):
	return """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>%s</title>
%s
</head>
<body>
%s
</body>
</html>
""" % (escape(title), headers, content)

# from urlparse import urlparse, parse_qs
# uri = urlparse(self.path.lstrip('/'))
# filepath = os.path.normpath(uri.path)
# query = parse_qs(uri.query)

# Some URL parsing helper functions
def getPathFromURL(url):
	temp = url.split('/', 1)[1] # Split away the domain name
	return temp.split('?', 1)[0] # Return everything before the query.

def getQueryDictFromURL(url):
	query = None
	temp = url.rsplit('?', 1)
	if len(temp) == 1:
		# No query string!
		query = {}
	else:
		temp = temp[1].rsplit('#', 1)[0] # Split away fragment id
		temp = temp.replace('=', '":"').replace('&', '","') # Turn into python dictonary syntax
		query = eval('{"' + temp + '"}')
		
		# Un-percent encode query items
		for k in query:
			temp = query[k].split('%')
			for i in range(1, len(temp)):
				temp[i] = eval('"\\x' + temp[i][:2] + '"') + temp[i][2:]
			query[k] = ''.join(temp)
	
	return query

# The server
class MyHandler(BaseHTTPRequestHandler):
	# Customize error messages a bit; not important
	def send_error(self, code, message=None):
		self.send_response(code)
		self.send_header('Content-Type', self.error_content_type)
		self.end_headers()
		content = "<h1>%d %s</h1>" % (code, self.responses[code][0] if message == None else message)
		self.wfile.write(makepage("Error %d" % code, content))
	
	# This is the main function
	def do_GET(self):
		try:
			
			# Parse the URL
			filepath = getPathFromURL(self.path)
			query = getQueryDictFromURL(self.path)
			
			if not path.exists(filepath):
				# Non-existent file!
				self.send_error(404)
			
			elif filepath in ('index.html', 'stage1.html', 'stage2.html', 'stage3.html', 'stage4.html'):
				self.send_response(200)
				self.send_header('Content-type','text/html')
				self.end_headers()
				with open(filepath) as f:
					self.wfile.write(f.read())
			
			elif filepath=='task4.py':
				self.send_response(200)
				self.send_header('Content-type','text/plain')
				self.end_headers()
				with open(filepath) as f:
					self.wfile.write(f.read())
				
			else:
				# Now allowed!
				self.send_error(403)
		
		except:
			# Show people the mess they caused!
			self.send_response(500)
			self.send_header('Content-type','text/html')
			self.end_headers()
			from sys import exc_type
			self.wfile.write(makepage("Traceback %s" % str(exc_type), "<pre>%s</pre>" % escape(traceback.format_exc())))

# To make it easier to play around with this, we'll communicate over stdin/stdout
# like the other exercises instead of listening and forking like a real server.
# A program external to this script handles turning it into a network service.

class MyStdioHandler(MyHandler):
  def __init__(self):
    MyHandler.__init__(self, None, 'derp', None)
  def setup(self):
    self.rfile = stdin
    self.wfile = stdout
  def log_message(format, *args):
    pass

MyStdioHandler()

#
# Instead of the above ~10 lines of code, the following turns this
# script into a server on its own.
#
# Serves multiple requests at the same time
# class ForkingHTTPServer(ForkingMixIn, HTTPServer):
#   timeout = 10
#   max_children = 1000
#
# if __name__ == "__main__":
#   server = ForkingHTTPServer(('', 6364), MyHandler)
#   try:
#     print "Server started on port {0.server_port}, press <Ctrl-C> to exit.".format(server)
#     server.serve_forever()
#   except KeyboardInterrupt:
#     pass
#   finally:
#     server.server_close()
#   print "Server closed."
