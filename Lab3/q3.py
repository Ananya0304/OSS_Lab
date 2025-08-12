def n_largest_elements(lst, n):
    return sorted(lst, reverse=True)[:n]

numbers = [4, 1, 7, 3, 9, 2]
print(n_largest_elements(numbers, 3))
