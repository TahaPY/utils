import base64


def b64_decode(data):
    return base64.b64decode(data).decode("utf8")
