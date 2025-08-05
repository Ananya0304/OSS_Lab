def triplet(n):
    result = []
    for a in range(n):
        for b in range(a, n):  # b starts from a to avoid duplicates
            c = a + b
            if c < n:
                result.append((a, b, c))
    return result

# Example usage
print(triplet(10))
