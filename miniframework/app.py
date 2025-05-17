from __future__ import annotations

from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Callable, List

from .request import Request
from .response import Response
from .router import Router

Middleware = Callable[[Request, Response, Callable[[], None]], None]
Handler = Callable[[Request, Response], None]


class MiniFramework:
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
        req = Request(handler)
        res = Response(handler)
        index = 0

        def next_middleware() -> None:
            nonlocal index
            if index < len(self.middleware):
                current = self.middleware[index]
                index += 1
                current(req, res, next_middleware)
            else:
                route_handler, params = self.router.match(req.method, req.path)
                if route_handler:
                    req.params = params
                    route_handler(req, res)
                else:
                    res.send("Not Found", status=404)

        next_middleware()

    def listen(self, host: str = "127.0.0.1", port: int = 8000) -> None:
        app = self

        class RequestHandler(BaseHTTPRequestHandler):
            def do_GET(self) -> None:
                app._handle(self)

            def do_POST(self) -> None:
                app._handle(self)

            def log_message(self, format: str, *args) -> None:  # pragma: no cover
                return

        httpd = HTTPServer((host, port), RequestHandler)
        print(f"Serving on http://{host}:{port}")
        httpd.serve_forever()
