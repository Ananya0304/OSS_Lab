def lensort(strings):
    return sorted(strings, key=len)

# Example usage
words = ["apple", "fig", "banana", "kiwi", "grape"]
print("Sorted by length:", lensort(words))
