from typing import Callable, Dict, List, Optional, Tuple


class Router:
    """Simple route registry and matcher."""

    def __init__(self) -> None:
        self.routes: List[Tuple[str, str, Callable]] = []

    def add_route(self, method: str, path: str, handler: Callable) -> None:
        self.routes.append((method.upper(), path, handler))

    def match(self, method: str, path: str) -> Tuple[Optional[Callable], Dict[str, str]]:
        for route_method, route_path, handler in self.routes:
            params = self._match_path(route_path, path)
            if route_method == method and params is not None:
                return handler, params
        return None, {}

    def _match_path(self, route_path: str, request_path: str) -> Optional[Dict[str, str]]:
        route_parts = route_path.strip('/').split('/')
        request_parts = request_path.strip('/').split('/')
        if len(route_parts) != len(request_parts):
            return None
        params: Dict[str, str] = {}
        for route_part, req_part in zip(route_parts, request_parts):
            if route_part.startswith(':'):
                params[route_part[1:]] = req_part
            elif route_part != req_part:
                return None
        return params
