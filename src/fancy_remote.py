import http.server
import os
import urllib.parse
import html
import sys
import io
import subprocess

AUTHOR = "Norton Pengra"
DATE_CREATED = "July 5, 2016"
VERSION = 0.1

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
        r.append('<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.0.0/jquery.min.js"></script>')
        r.append("""
            <style>
            html, body {
                padding: 0;
                margin: 0;
                background: #fff;
                color: #232323;
                font-family: Verdana;
            }
            div.files {
                width: 80%;
                margin: auto;
            }
            div.icon {
                width: 100px; height: 100px;
                background: #0078d7;
                color: #fff;
                padding: 10px;
                margin: 5px;
                float: left;
            }
            header {
                background: #232323;
                color: #fff;
                text-align: center;
                padding-top: 5px;
                padding-bottom: 5px;
                margin-bottom: 20px;
            }
            footer {
                position: fixed;
                left: 0;
                right: 0;
                bottom: 0;
                height: 50px;
                background: #232323;
                color: #fff;
                text-align: center;
            }
            </style>
        """)
        r.append('<title>{}</title>'.format(title))
        r.append('</head>')
        r.append('<body>')
        r.append('<header>{}</header>'.format(title))
        r.append('<div class="files">')
        for name in list:
            fullname = os.path.join(path, name)
            displayname = linkname = name
            state = "file"
            if os.path.isdir(fullname):
                displayname = name + "/"
                linkname = name + "/"
                state = "dir"
            if os.path.islink(fullname):
                displayname = name + "@"
                state += "_link"
            r.append('<a href="{}"><div class="icon {}">'.format(linkname, state))
            if state.startswith("dir"):
                r.append('<img src="http://www.iconarchive.com/download/i32/3xhumed/cryonic-folder/Folder-Blank-1.ico" width="75px" height="75px">')
            elif state.startswith('file'):
                r.append('<img src="http://www.iconarchive.com/download/i83626/pelfusion/flat-file-type/txt.ico" width="75px" width="75px">')
            r.append('<span>{}</span>'.format(displayname))
            r.append('</div></a>')

        r.append('</div>')
        r.append('<footer>')
        r.append("Coded with love by Norton ")
        r.append('</footer>')
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
