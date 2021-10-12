from typing import Optional


def add_url_params(url: str, params: dict[str, Optional[str]]) -> str:
    """Helps for combining parameters with url."""
    result = (
        f'{key}={value}'
        for key, value in params.items()
        if value
    )
    return f"{url}?{'&'.join(result)}"


def group_by_n(list_: list, n: int) -> list[list]:
    result = []
    temporary_list = []
    for j in list_:
        temporary_list.append(j)
        if len(temporary_list) == n:
            result.append(temporary_list)
            temporary_list = []
    if temporary_list:
        result.append(temporary_list)
    return result


print(group_by_n([4, 5, 8, 9, 8, 5], 4))
