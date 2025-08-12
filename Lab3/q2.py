def valuesort(d):
    return [d[key] for key in sorted(d)]

data = {'b': 2, 'a': 1, 'c': 3}
print(valuesort(data))
