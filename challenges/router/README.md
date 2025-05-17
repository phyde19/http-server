# Router Challenge

In this challenge you will build Sparrow's routing system.

## Goal

Implement the three missing methods inside `sparrow/router.py`.

### Tasks

1. **add_route** - store a tuple of `(method, normalized_path, handler)` so routes can be looked up later.
2. **match** - iterate over registered routes returning the handler and any parameters once a path matches.
3. **_match_path** - compare route paths against incoming request paths.  Support parameters prefixed with `:` and return them as a dictionary.

### Example

```python
router = Router()

def hello(req, res):
    pass

router.add_route('GET', '/hello/:name', hello)
handler, params = router.match('GET', '/hello/bob')
assert handler is hello
assert params == {'name': 'bob'}
```

Run `pytest` to verify your work once you've completed the implementation.
