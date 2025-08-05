def parse_csv(filename):
    with open(filename, 'r') as file:
        return [line.strip().split(',') for line in file]

# Example usage
# parsed = parse_csv('data.csv')
# print(parsed)
import string

def mutate(word):
    mutations = set()
    letters = string.ascii_lowercase

    # Insert
    for i in range(len(word) + 1):
        for c in letters:
            mutations.add(word[:i] + c + word[i:])

    # Delete
    for i in range(len(word)):
        mutations.add(word[:i] + word[i+1:])

    # Replace
    for i in range(len(word)):
        for c in letters:
            mutations.add(word[:i] + c + word[i+1:])

    # Swap
    for i in range(len(word) - 1):
        swapped = list(word)
        swapped[i], swapped[i+1] = swapped[i+1], swapped[i]
        mutations.add(''.join(swapped))

    return list(mutations)

# Example usage
# print(mutate("cat"))
