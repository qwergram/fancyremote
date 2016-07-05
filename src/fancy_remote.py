import http.server


AUTHOR = "Norton Pengra"
DATE_CREATED = "July 5, 2016"
VERSION = 0.0


class BootstrapFileNav(http.server.SimpleHTTPRequestHandler):

	server_version = "PengraBot/" + str(VERSION)

	def list_directory(self, path):
		return super().list_directory(path)


if __name__ == "__main__":
	http.server.test(HandlerClass=BootstrapFileNav, port=8080)
