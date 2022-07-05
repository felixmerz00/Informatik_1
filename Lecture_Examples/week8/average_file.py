def average(values):
    if values == []: return None
    sum = 0
    for v in values: sum += v
    return sum / len(values)