# Request Challenge

Complete the body parsing logic inside `Request._read_body` located in `sparrow/request.py`.

## Goal

Read the raw body from the HTTP handler and expose the parsed value via `Request.body`.

### Tasks

1. Read the body using the `Content-Length` header.
2. If the `Content-Type` contains `application/json`, decode the text and parse it with `json.loads`. When parsing fails return `None`.
3. For any other content type simply decode the bytes as UTF-8.

### Example

```python
headers = {
    'Content-Length': '13',
    'Content-Type': 'application/json'
}
handler = DummyHandler(body=b'{"a":1}', headers=headers)
req = Request(handler)
assert req.body == {"a": 1}
```

Use the provided tests (`pytest`) to verify your implementation.
