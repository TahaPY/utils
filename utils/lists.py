from itertools import islice


def chunks(arr, n):
    """
    Yield successive n-sized chunks from arr.
    :param arr
    :param n
    :return generator
    """
    for i in range(0, len(arr), n):
        yield arr[i:i + n]


def take(arr, n):
    """
    Returns n element of the arr.
    :param arr:
    :param n:
    :return: list of n element
    """
    return list(islice(arr, n))
