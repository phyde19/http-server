# Application Challenge

The `Sparrow` class ties everything together. Completing these methods will give you a working micro framework.

## Tasks

1. **_handle**
   - Construct `Request` and `Response` objects for the incoming `handler`.
   - Execute middleware in the order registered. Each middleware receives `next()` to continue the chain.
   - After middleware, find the matching route and invoke it with `(req, res)`.
   - If no route matches, respond with a 404.
2. **listen**
   - Create an `HTTPServer` bound to `host` and `port` using a custom `BaseHTTPRequestHandler` subclass.
   - In each HTTP verb method (`do_GET`, `do_POST`, ...), delegate to `_handle`.
   - Suppress the default logging output from `BaseHTTPRequestHandler` for cleaner test runs.

### Example

Running `example_server.py` should start a server on port 8080 once these pieces are implemented.

Execute `pytest -k app -v` to run application-specific tests.
=======
Two key methods in `sparrow/app.py` are intentionally incomplete:

1. `_handle` orchestrates middleware execution, route lookup and dispatching.
2. `listen` sets up an `HTTPServer` and binds request methods to `_handle`.

Implement both methods so that the example server and tests function correctly. When finished, run `pytest` to check your work.
