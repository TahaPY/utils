def chunks(arr, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(arr), n):
        yield arr[i:i + n]
