# Request Challenge

Requests come from the web server with headers and a raw body stream. Implement `_read_body` so the framework can conveniently access that data.

## Tasks

1. Use the `Content-Length` header to read exactly that many bytes from `handler.rfile`.
2. Inspect `Content-Type`:
   - When it contains `application/json`, decode the bytes as UTF-8 and parse with `json.loads`. Return `None` if parsing fails.
   - Otherwise decode the bytes to a UTF-8 string.
3. If no body is present, return `None`.

### Example

A POST with JSON:

```http
POST /echo HTTP/1.1
Content-Type: application/json
Content-Length: 13

{"msg": "hi"}
```

Should set `req.body` to `{"msg": "hi"}`.

Run `pytest -k request -v` once this function is complete.
