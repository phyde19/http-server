import io
import unittest
from http.server import BaseHTTPRequestHandler
from sparrow.response import Response


class DummyHandler(BaseHTTPRequestHandler):
    def __init__(self):
        self.wfile = io.BytesIO()
        self.headers_sent = []

    def send_response(self, status):
        self.status = status

    def send_header(self, name, value):
        self.headers_sent.append((name, value))

    def end_headers(self):
        pass


class ResponseTests(unittest.TestCase):
    def test_json_helper(self):
        handler = DummyHandler()
        res = Response(handler)
        res.json({'ok': True}, status=201)
        handler.wfile.seek(0)
        body = handler.wfile.read().decode()
        print('Response body:', body)
        self.assertEqual(handler.status, 201)
        self.assertIn(('Content-Type', 'application/json'), handler.headers_sent)
        self.assertIn('"ok": true', body)


if __name__ == '__main__':
    unittest.main()
