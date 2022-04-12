
def decimal_range(start, stop, increment):
    while start <= stop: # and not math.isclose(start, stop): Py>3.5
        yield start
        start += increment