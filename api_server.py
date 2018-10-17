import http.server
import json


class API_Handler(http.server.BaseHTTPRequestHandler):

    def do_POST(self):
        # print(self.headers['content-type'], self.headers['content-length'])
        if self.headers['content-type'] == 'application/json':
            length = int(self.headers['content-length'])
            post_values = json.loads(self.rfile.read(length))
        else:
            self.send_response(200)
            self.send_header('content-type', 'application/json')
            self.end_headers()
            self.response = {'response': 'only json'}
            self.wfile.write(json.dumps(self.response))
            return

        # print('POST_VALUE=', post_values)
        if post_values['request'] == "Hello":
            self.response = {'response': 'ok'}
        else:
            self.response = {'response': 'error'}

        self.send_response(200)
        self.send_header('content-type', 'application/json')
        self.end_headers()

        self.wfile.write(json.dumps(self.response).encode('utf-8'))


server = http.server.HTTPServer(('localhost', 8888), API_Handler)
print('Starting server, use <Ctrl-C> to stop')
server.serve_forever()
