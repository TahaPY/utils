from typing import Union


def is_null_or_empty(string: Union[str, None]) -> bool:
    """
    Is checking string is none or empty
    :param string:
    :return: bool
    """
    return string is None or string == ""
