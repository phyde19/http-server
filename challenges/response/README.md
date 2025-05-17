# Response Challenge

Fill in the response helpers defined in `sparrow/response.py`.

- `send` must handle status codes, headers, and sending both text and JSON bodies.
- Ensure the response is only sent once.
- `json` should serialize the given object and delegate to `send`.

Run `pytest` when you think you are done.
