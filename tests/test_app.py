import io
import unittest
from sparrow import Sparrow


class AppTests(unittest.TestCase):
    def test_middleware_and_routing(self):
        calls = []
        app = Sparrow()

        @app.use
        def mw(req, res, next_func):
            calls.append('mw')
            next_func()

        @app.get('/ping')
        def handler(req, res):
            calls.append('handler')
            res.send('pong')

        # Use internal pieces without running a server
        class Dummy:
            def __init__(self):
                self.command = 'GET'
                self.path = '/ping'
                self.headers = {}
                self.rfile = io.BytesIO()
                self.wfile = io.BytesIO()
        dummy = Dummy()
        app._handle(dummy)
        dummy.wfile.seek(0)
        body = dummy.wfile.read().decode()
        print('Middleware calls:', calls)
        print('Body:', body)
        self.assertEqual(body, 'pong')
        self.assertEqual(calls, ['mw', 'handler'])


if __name__ == '__main__':
    unittest.main()
