from __future__ import annotations

import json
from http.server import BaseHTTPRequestHandler
from typing import Any, Dict, Optional
from urllib.parse import parse_qs, urlparse


class Request:
    """HTTP request wrapper."""

    def __init__(self, handler: BaseHTTPRequestHandler) -> None:
        self.method: str = handler.command
        self.headers = handler.headers
        parsed = urlparse(handler.path)
        self.path: str = parsed.path
        self.query: Dict[str, Any] = {k: v[0] if len(v) == 1 else v for k, v in parse_qs(parsed.query).items()}
        self.body: Optional[Any] = self._read_body(handler)
        self.params: Dict[str, str] = {}

    def _read_body(self, handler: BaseHTTPRequestHandler) -> Optional[Any]:
        """Read and parse the request body."""
        # TODO: use the ``Content-Length`` header to read the request body from
        # ``handler.rfile``. If the content type is JSON, decode and return the
        # parsed object. Otherwise return the decoded text. If no body is
        # present, return ``None``.
        raise NotImplementedError
