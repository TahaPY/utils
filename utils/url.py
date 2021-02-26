def join(*args):
    """
    join url with paths and url queries
    :param args:
    :return:
    """
    return '/'.join([arg.rstrip('/') for arg in args if len(arg)])
