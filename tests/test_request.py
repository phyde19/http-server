import io
import unittest

from sparrow.request import Request


class DummyHandler:
    def __init__(self, method='POST', path='/', headers=None, body=b''):
        self.command = method
        self.path = path
        self.headers = headers or {}
        self.rfile = io.BytesIO(body)


class RequestChallengeTests(unittest.TestCase):
    def test_json_body(self):
        print("Request JSON body parsing")
        headers = {'Content-Length': '13', 'Content-Type': 'application/json'}
        handler = DummyHandler(body=b'{"foo": "bar"}', headers=headers)
        req = Request(handler)
        self.assertEqual(req.body, {"foo": "bar"})

    def test_text_body(self):
        print("Request text body parsing")
        headers = {'Content-Length': '11', 'Content-Type': 'text/plain'}
        handler = DummyHandler(body=b'hello world', headers=headers)
        req = Request(handler)
        self.assertEqual(req.body, "hello world")


if __name__ == '__main__':
    unittest.main()
