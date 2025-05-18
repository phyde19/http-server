import unittest
from sparrow.router import Router


def dummy(req, res):
    pass


class RouterTests(unittest.TestCase):
    def test_add_and_match(self):
        router = Router()
        router.add_route('GET', '/hello/:name', dummy)
        handler, params = router.match('GET', '/hello/world')
        print('Matched params:', params)
        self.assertIs(handler, dummy)
        self.assertEqual(params, {'name': 'world'})


if __name__ == '__main__':
    unittest.main()
