import base64


def b64_encode(data):
    return base64.b64encode(data).encode("utf8")
