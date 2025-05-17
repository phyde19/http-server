from typing import Callable, Dict, List, Optional, Tuple


class Router:
    """Simple route registry and matcher."""

    def __init__(self) -> None:
        self.routes: List[Tuple[str, str, Callable]] = []

    def add_route(self, method: str, path: str, handler: Callable) -> None:
        """Register a new route."""
        # TODO: store the method, normalized path and handler so that it can be
        # matched later in ``match``.
        raise NotImplementedError

    def match(self, method: str, path: str) -> Tuple[Optional[Callable], Dict[str, str]]:
        """Return the first matching handler and extracted parameters."""
        # TODO: iterate over registered routes and use ``_match_path`` to
        # determine if the path matches. Return the handler and parameters when
        # a match is found or ``(None, {})`` otherwise.
        raise NotImplementedError

    def _match_path(self, route_path: str, request_path: str) -> Optional[Dict[str, str]]:
        """Compare a route path against a request path."""
        # TODO: split the paths and compare each segment. Support parameters
        # prefixed with ':' in the route path and return them in a dictionary
        # when the paths match. Return ``None`` if they do not match.
        raise NotImplementedError
