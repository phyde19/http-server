# Router Challenge

Implement the routing logic in `sparrow/router.py`.

- `add_route` should register a new route for a specific HTTP method and path.
- `match` must return the handler and any extracted parameters for the first route that matches the given method and path.
- `_match_path` compares a stored route path with a request path and returns a dictionary of parameter values or `None` if they do not match.

Run `pytest` after completing this challenge to ensure your implementation works.
