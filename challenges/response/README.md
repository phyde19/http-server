# Response Challenge

Fill in the response helpers defined in `sparrow/response.py`.

## Goal

Provide a simple API for sending HTTP responses from handlers.

### Tasks

1. **send** - write the status line, headers, and body to the underlying `BaseHTTPRequestHandler`. If the body is a dictionary or list, serialize it with `json.dumps` and set `Content-Type` to `application/json`. Strings should be encoded as UTF-8. Prevent multiple calls from sending multiple responses.
2. **json** - convenience wrapper that serializes the object and delegates to `send`.

### Example

```python
res.send('hello', status=200)
res.json({'ok': True})
```

Run `pytest` when you think you are done.
