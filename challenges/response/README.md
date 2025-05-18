# Response Challenge

Responses send data back to the client. Implement helper methods so your handlers can easily reply with text or JSON.

## Tasks

1. **send**
   - Write the HTTP status code and any headers.
   - If `body` is a `dict` or `list`, serialize it with `json.dumps` and set `Content-Type` to `application/json` unless already provided.
   - Encode string bodies as UTF-8 bytes.
   - Only allow a single call per request (ignore subsequent calls).
2. **json**
   - Convenience wrapper that serializes `obj` and forwards to `send`.

### Example

```python
res.send("ok")
res.json({"status": "ok"}, status=201)
```

Use `pytest -k response -v` after implementing these functions.
=======
Fill in the response helpers defined in `sparrow/response.py`.

- `send` must handle status codes, headers, and sending both text and JSON bodies.
- Ensure the response is only sent once.
- `json` should serialize the given object and delegate to `send`.

Run `pytest` when you think you are done.
