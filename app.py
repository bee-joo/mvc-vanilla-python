from http.server import HTTPServer, BaseHTTPRequestHandler
from jinja2 import Environment, PackageLoader, select_autoescape
import urllib.parse
import mimetypes
import models.client as model 
import sys


env = Environment(
    loader=PackageLoader('app', 'templates'),
    autoescape=select_autoescape(['html', 'xml']))

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        import views.client as view

        data = model.DB('data.sqlite')
        
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html, charset="utf-8"')
            self.end_headers()

            result = view.client_view.render_get_form()
            result = bytes(result, 'utf-8')

            self.wfile.write(result)

        
        elif self.path.startswith('/users/') and self.path.endswith('/'):
            
            id = self.path[len(self.path.rstrip('0123456789/')):].strip('/')
            
            if id == "":
                self.send_response(200)
                self.send_header('Content-Type', 'text/html, charset="utf-8"')
                self.end_headers()
                
                result = view.client_view.render_all_users()
                result = bytes(result, 'utf-8')

                self.wfile.write(result)

            else:
                user = data.get_by_id(id)

                if user == None:
                    self.do_404()

                else:
                    self.send_response(200)
                    self.send_header('Content-Type', 'text/html, charset="utf-8"')
                    self.end_headers()

                    result = view.client_view.render_user_page(user, id)
                    result = bytes(result, 'utf-8')

                    self.wfile.write(result)
   

        elif self.path.startswith('/images/') and self.path.endswith('.svg/'):
            filename = self.path.lstrip('/').rstrip('/')

            try:
                imgfile = open(filename, 'rb').read()
            except Exception:
                self.do_404()
            else:
                mimetype = mimetypes.MimeTypes().guess_type(filename)[0]
                self.send_response(200)
                self.send_header('Content-type', mimetype)
                self.end_headers()
                self.wfile.write(imgfile)

        else:
            self.do_404()
            


    def do_POST(self):
        
        import views.client as view
        
        self.send_response(200)
        self.send_header('Content-Type', 'text/html, charset="utf-8"')
        self.end_headers()

        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        body = urllib.parse.parse_qs(str(body, 'utf-8'))

        result = view.client_view.render_post(body)
        result = bytes(result,'utf-8')

        self.wfile.write(result)

    
    def do_404(self):

        import views.client as view

        self.send_response(404)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()

        result = view.client_view.render_404()
        result = bytes(result, 'utf-8')
        self.wfile.write(result)


try:
    httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
    print("Serving on localhost:8000")
    httpd.serve_forever()

except KeyboardInterrupt:
    print("Stopping server")
    sys.exit(0)
