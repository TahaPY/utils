import base64


def b64_encode(data: bytes):
    return base64.b64encode(data).decode("utf8")
