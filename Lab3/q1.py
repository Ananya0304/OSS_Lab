def invertdict(d):
    return {value: key for key, value in d.items()}

original = {'a': 1, 'b': 2, 'c': 3}
inverted = invertdict(original)
print(inverted)  
