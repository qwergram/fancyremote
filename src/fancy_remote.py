import http.server
import os
import urllib.parse
import html
import sys
import io

AUTHOR = "Norton Pengra"
DATE_CREATED = "July 5, 2016"
VERSION = 0.0

os.chdir('/')

class BootstrapFileNav(http.server.SimpleHTTPRequestHandler):

	server_version = "PengraBot/" + str(VERSION)

	def list_directory(self, path):
		try:
			list = os.listdir(path)
		except OSError:
			self.send_error(404, "No permission to list directory")
			return None
		list.sort(key=lambda a: a.lower())
		r = []
		try:
			displaypath = urllib.parse.unquote(self.path, errors="surrogatepass")
		except UnicodeDecodeError:
			displaypath = urllib.parse.unquote(path)
		displaypath = html.escape(displaypath)
		enc = sys.getfilesystemencoding()
		title = "Directory listing for {}".format(displaypath)
		r.append('<!DOCTYPE html')
		r.append('<html>\n<head>')
		r.append('<title>{}</title>'.format(title))
		r.append('</head>')
		r.append('<body>')
		r.append('<h1>Hello</h1>')

		# Do logic stuff here

		r.append('</body></html')

		encoded = "\n".join(r).encode(enc, 'surrogateescape')
		f = io.BytesIO()
		f.write(encoded)
		f.seek(0)
		self.send_response(200)
		self.send_header("Content-type", "text/html; charset={}".format(enc))
		self.send_header("Content-Length", str(len(encoded)))
		self.end_headers()
		return f

		# return super().list_directory(path)


if __name__ == "__main__":
	http.server.test(HandlerClass=BootstrapFileNav, port=8080)
