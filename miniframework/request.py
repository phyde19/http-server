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
        length = int(handler.headers.get('Content-Length', 0))
        if length == 0:
            return None
        data = handler.rfile.read(length)
        content_type = handler.headers.get('Content-Type', '')
        if 'application/json' in content_type:
            try:
                return json.loads(data)
            except json.JSONDecodeError:
                return None
        return data.decode('utf-8')
