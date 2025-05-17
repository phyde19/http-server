import io
import unittest

from sparrow.response import Response


class DummyHandler:
    def __init__(self):
        self.status = None
        self.sent_headers = []
        self.wfile = io.BytesIO()

    def send_response(self, status):
        self.status = status

    def send_header(self, name, value):
        self.sent_headers.append((name, value))

    def end_headers(self):
        pass


class ResponseChallengeTests(unittest.TestCase):
    def test_send_text(self):
        print("Response send text")
        handler = DummyHandler()
        res = Response(handler)
        res.send("hi")
        self.assertEqual(handler.status, 200)
        self.assertEqual(handler.wfile.getvalue().decode(), "hi")

    def test_send_json(self):
        print("Response send json")
        handler = DummyHandler()
        res = Response(handler)
        res.json({"a": 1})
        body = handler.wfile.getvalue().decode()
        headers = dict(handler.sent_headers)
        self.assertIn("application/json", headers.get("Content-Type", ""))
        self.assertIn('"a": 1', body)


if __name__ == '__main__':
    unittest.main()
