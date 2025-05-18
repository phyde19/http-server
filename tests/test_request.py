import io
import unittest
from http.server import BaseHTTPRequestHandler
from sparrow.request import Request


class DummyHandler(BaseHTTPRequestHandler):
    def __init__(self, body=b'', headers=None):
        self.rfile = io.BytesIO(body)
        self.wfile = io.BytesIO()
        self.command = 'POST'
        self.path = '/'
        self.headers = headers or {}

    def send_error(self, code, message=None):
        pass


class RequestTests(unittest.TestCase):
    def test_json_body(self):
        headers = {
            'Content-Length': '13',
            'Content-Type': 'application/json'
        }
        handler = DummyHandler(body=b'{"a":1}', headers=headers)
        req = Request(handler)
        print('Parsed body:', req.body)
        self.assertEqual(req.body, {'a': 1})


if __name__ == '__main__':
    unittest.main()
