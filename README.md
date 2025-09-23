# EX01 Developing a Simple Webserver
## Date: 08.09.2025

## AIM:
To develop a simple webserver to serve html pages and display the Device Specifications of your Laptop.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
 <html>
    <head>
        <title>
            my webserver
        </title>
    </head>
    <body>
    <caption><b>A.MONIGA (25017526) </b></caption>
        <table border="5" cellpadding="3"
        <tr>
            <th>S.No</th>
            <th>Data specifications</th>
            <th>Type</th>
        </tr>
        <tr>
            <td>1</td>
            <td>Device name</td>
            <td>TMP765-75-G2</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Processor</td>
            <td>Intel(R) Core(TM) Ultra 5 125H(1.50 GHz)</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Installed RAM</td>
            <td>16.0 GB (16.5 GB usable)</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Device ID</td>
            <td>E3F06795-1915-4187-8C56-F3F3634559FF</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Product ID</td>
            <td>00469-42674-08438-AAOEM</td>
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

```
## OUTPUT:
![alt text](<Screenshot (31) copy.png>)
![alt text](<Screenshot (32).png>)
## RESULT:
The program for implementing simple webserver is executed successfully.
