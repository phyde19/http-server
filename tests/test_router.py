import unittest
from sparrow.router import Router


def dummy(req, res):
    pass


class RouterChallengeTests(unittest.TestCase):
    def test_static_route(self):
        print("Router static route test")
        r = Router()
        r.add_route('GET', '/foo', dummy)
        handler, params = r.match('GET', '/foo')
        self.assertIs(handler, dummy)
        self.assertEqual(params, {})

    def test_param_route(self):
        print("Router parameter test")
        r = Router()
        r.add_route('GET', '/user/:id', dummy)
        handler, params = r.match('GET', '/user/42')
        self.assertIs(handler, dummy)
        self.assertEqual(params, {'id': '42'})


if __name__ == '__main__':
    unittest.main()
