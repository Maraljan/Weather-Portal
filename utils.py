from typing import Optional


def add_url_params(url: str, params: dict[str, Optional[str]]) -> str:
    result = (
        f'{key}={value}'
        for key, value in params.items()
        if value
    )
    return f"{url}?{'&'.join(result)}"
