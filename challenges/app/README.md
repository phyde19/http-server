# Application Challenge

Two key methods in `sparrow/app.py` are intentionally incomplete:

1. `_handle` orchestrates middleware execution, route lookup and dispatching.
2. `listen` sets up an `HTTPServer` and binds request methods to `_handle`.

Implement both methods so that the example server and tests function correctly. When finished, run `pytest` to check your work.
