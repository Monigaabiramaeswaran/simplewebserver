from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
 <html>
    <head>
        <title>
            Tabular column
        </title>
    </head>
    <body>
        <table border="5" cellpadding="3"
        <tr>
            <th>S.No</th>
            <th>Data specifications</th>
            <th>Type</th>
        </tr>
        <tr>
            <td>1</td>
            <td>Device name</td>
            <td>TMP215-75-G2</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Processor</td>
            <td>Intel(R) Core(TM) Ultra 5 125H(1.20 GHz)</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Installed RAM</td>
            <td>16.0 GB (15.5 GB usable)</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Device ID</td>
            <td>E3F06795-1915-4187-8C56-F3F3634559FF</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Product ID</td>
            <td>00342-42784-08438-AAOEM</td>
        </tr>
    </body>
</html>
         
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()