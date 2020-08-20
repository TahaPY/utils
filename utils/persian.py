import re

digits = {
    "0": "۰",
    "1": "۱",
    "2": "۲",
    "3": "۳",
    "4": "۴",
    "5": "۵",
    "6": "۶",
    "7": "۷",
    "8": "۸",
    "9": "۹",
}


def convert_digits(string: str) -> str:
    pattern = re.compile("|".join(digits.keys()))
    return pattern.sub(lambda x: digits[x.group()], string)
