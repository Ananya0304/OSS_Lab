def duplicate(numbers):
    seen = set()
    duplicates = set()
    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)

nums = [1, 2, 3, 4, 5, 3, 6, 7, 2, 8]
print("Duplicates:", duplicate(nums))
