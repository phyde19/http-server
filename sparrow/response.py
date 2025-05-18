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
        """Send a response to the client."""
        # TODO: write the HTTP status and headers using ``self._handler``. If
        # ``body`` is a dict or list, serialize it as JSON and set the
        # ``Content-Type`` header appropriately. Encode strings as UTF-8 before
        # writing and ensure the response is only sent once.
        raise NotImplementedError

    def json(self, obj: Any, status: int = 200, headers: Dict[str, str] | None = None) -> None:
        """Convenience method for sending JSON data."""
        # TODO: serialize ``obj`` to JSON and call ``send`` with the correct
        # headers.
        raise NotImplementedError
