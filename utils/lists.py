def chunks(arr, n):
    """
    Yield successive n-sized chunks from arr.
    :param arr
    :param n
    :return generator
    """
    for i in range(0, len(arr), n):
        yield arr[i:i + n]
