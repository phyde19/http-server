from __future__ import annotations

from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Callable, List

from .request import Request
from .response import Response
from .router import Router

Middleware = Callable[[Request, Response, Callable[[], None]], None]
Handler = Callable[[Request, Response], None]


class Sparrow:
    """A minimal HTTP framework to demonstrate request handling."""

    def __init__(self) -> None:
        self.router = Router()
        self.middleware: List[Middleware] = []

    # Route decorators
    def route(self, path: str, methods: List[str]) -> Callable[[Handler], Handler]:
        def decorator(func: Handler) -> Handler:
            for method in methods:
                self.router.add_route(method.upper(), path, func)
            return func
        return decorator

    def get(self, path: str) -> Callable[[Handler], Handler]:
        return self.route(path, ["GET"])

    def post(self, path: str) -> Callable[[Handler], Handler]:
        return self.route(path, ["POST"])

    def use(self, func: Middleware) -> None:
        self.middleware.append(func)

    def _handle(self, handler: BaseHTTPRequestHandler) -> None:
        """Handle a single HTTP request."""
        # TODO: create ``Request`` and ``Response`` objects, run middleware in
        # order and dispatch to the matched route handler. Send a 404 response
        # when no route matches.
        raise NotImplementedError

    def listen(self, host: str = "127.0.0.1", port: int = 8000) -> None:
        """Start an HTTP server to serve requests."""
        # TODO: create an ``HTTPServer`` instance that uses a custom
        # ``BaseHTTPRequestHandler`` subclass. The handler methods should call
        # ``_handle`` for each incoming request and suppress default logging.
        raise NotImplementedError
