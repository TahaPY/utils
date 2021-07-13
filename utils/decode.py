import base64


def b64_decode(data: str):
    return base64.b64decode(data).encode("utf8")
