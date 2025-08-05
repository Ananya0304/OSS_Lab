def custom_filter(func, lst):
    return [x for x in lst if func(x)]

# Example usage
print(custom_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))
