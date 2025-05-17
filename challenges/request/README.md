# Request Challenge

Complete the body parsing logic inside `Request._read_body` located in `sparrow/request.py`.

- Read the body from `handler.rfile` using the `Content-Length` header.
- If the `Content-Type` contains `application/json`, parse the body as JSON and return the resulting object. If parsing fails return `None`.
- For other content types, decode the body as UTF-8 text.

Use the provided tests (`pytest`) to verify your implementation.
