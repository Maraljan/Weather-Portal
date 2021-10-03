from typing import Optional


def add_url_params(url: str, params: dict[str, Optional[str]]) -> str:
    """Helps for combining parameters with url."""
    result = (
        f'{key}={value}'
        for key, value in params.items()
        if value
    )
    return f"{url}?{'&'.join(result)}"
