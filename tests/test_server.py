import http.client
import threading
import time
import unittest

from sparrow import Sparrow

app = Sparrow()

@app.get('/test')
def test_handler(req, res):
    res.send('ok')

@app.post('/mirror')
def mirror(req, res):
    res.json({'data': req.body})


def start_server():
    app.listen(host='127.0.0.1', port=9090)


def wait_for_server(port=9090, timeout=5):
    for _ in range(timeout * 10):
        conn = http.client.HTTPConnection('127.0.0.1', port)
        try:
            conn.request('GET', '/')
            conn.getresponse()
            conn.close()
            return True
        except Exception:
            time.sleep(0.1)
    return False


class ServerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        thread = threading.Thread(target=start_server, daemon=True)
        thread.start()
        assert wait_for_server()

    def test_get(self):
        conn = http.client.HTTPConnection('127.0.0.1', 9090)
        conn.request('GET', '/test')
        resp = conn.getresponse()
        body = resp.read().decode()
        conn.close()
        self.assertEqual(resp.status, 200)
        self.assertEqual(body, 'ok')
        print('GET route responded with:', body)

    def test_post_json(self):
        conn = http.client.HTTPConnection('127.0.0.1', 9090)
        headers = {'Content-Type': 'application/json'}
        conn.request('POST', '/mirror', body='{"foo": "bar"}', headers=headers)
        resp = conn.getresponse()
        data = resp.read().decode()
        conn.close()
        self.assertEqual(resp.status, 200)
        self.assertIn('"foo": "bar"', data)
        print('POST JSON echoed:', data)


if __name__ == '__main__':
    unittest.main()
