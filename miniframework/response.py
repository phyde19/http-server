from __future__ import annotations

import json
from http.server import BaseHTTPRequestHandler
from typing import Any, Dict


class Response:
    """HTTP response helper."""

    def __init__(self, handler: BaseHTTPRequestHandler) -> None:
        self._handler = handler
        self._sent = False

    def send(self, body: Any, status: int = 200, headers: Dict[str, str] | None = None) -> None:
        if self._sent:
            return
        self._handler.send_response(status)
        headers = headers or {}
        if isinstance(body, (dict, list)):
            headers.setdefault('Content-Type', 'application/json')
            body = json.dumps(body)
        for name, value in headers.items():
            self._handler.send_header(name, value)
        if isinstance(body, str):
            body = body.encode('utf-8')
        self._handler.send_header('Content-Length', str(len(body)))
        self._handler.end_headers()
        self._handler.wfile.write(body)
        self._sent = True

    def json(self, obj: Any, status: int = 200, headers: Dict[str, str] | None = None) -> None:
        headers = headers or {}
        headers.setdefault('Content-Type', 'application/json')
        self.send(json.dumps(obj), status=status, headers=headers)
