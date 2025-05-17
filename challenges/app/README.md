# Application Challenge

Two key methods in `sparrow/app.py` are intentionally incomplete.

## Goal

Wire together middleware execution, route dispatching and server start up.

### Tasks

1. **_handle** - create `Request` and `Response` instances, execute registered middleware in order and finally invoke the matched route handler. If no route matches, send a 404 response.
2. **listen** - create an `HTTPServer` using a custom `BaseHTTPRequestHandler` subclass. Its handler methods should delegate to `_handle` and suppress default logging.

### Example

When complete you should be able to run `example_server.py` and see responses for the registered routes.

Run `pytest` to ensure your implementation works as expected.
