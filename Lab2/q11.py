def custom_map(func, lst):
    return [func(x) for x in lst]

# Example usage
print(custom_map(lambda x: x * 2, [1, 2, 3, 4]))
