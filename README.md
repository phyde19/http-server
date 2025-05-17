# Sparrow - Minimal Python HTTP Framework

Sparrow is a minimal Python framework that demonstrates core concepts of a web framework.
It aims to show what happens when an HTTP request arrives and how the framework dispatches it to a route handler.

## Features

- Routing with path parameters
- Middleware support
- Request and response abstraction
- JSON body parsing and responses
- Simple server startup

## Example Usage

Run the provided example server:

```bash
python example_server.py
```

Then open `http://localhost:8080/hello` in your browser or use `curl`:

```bash
curl http://localhost:8080/hello
```

See `example_server.py` for more routes and usage examples.

## Coding Challenges

Several core functions have been replaced with TODOs. See the `challenges` directory for instructions on implementing the router, request parsing, response helpers and the main application logic.
