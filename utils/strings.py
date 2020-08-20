from typing import Union


def is_null_or_empty(string: Union[str, None]) -> bool:
    return string is None or string == ""
