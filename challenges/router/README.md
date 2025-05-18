# Router Challenge

The router stores all route handlers in the framework. Your goal is to build a tiny lookup system capable of matching paths with parameters, similar to what larger frameworks do.

## Tasks

1. **add_route**
   - Normalize the method to uppercase and store the tuple `(method, path, handler)`.
2. **match**
   - Search the registered routes for the first entry whose method and path match the request.
   - Return a tuple `(handler, params)` where `params` is a dictionary of any path parameters.
3. **_match_path**
   - Compare a route like `/users/:id` with a request path such as `/users/123`.
   - When all segments align, return `{"id": "123"}`; otherwise return `None`.

### Example

```python
router = Router()
router.add_route('GET', '/hello/:name', handler)
func, params = router.match('GET', '/hello/world')
# params == {'name': 'world'}
```

Run `pytest -k router -v` to execute just the router tests.
=======
Implement the routing logic in `sparrow/router.py`.

- `add_route` should register a new route for a specific HTTP method and path.
- `match` must return the handler and any extracted parameters for the first route that matches the given method and path.
- `_match_path` compares a stored route path with a request path and returns a dictionary of parameter values or `None` if they do not match.

Run `pytest` after completing this challenge to ensure your implementation works.
