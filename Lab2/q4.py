def group(lst, size):
    return [lst[i:i + size] for i in range(0, len(lst), size)]

# Example usage
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
grouped = group(data, 3)
print(grouped)
