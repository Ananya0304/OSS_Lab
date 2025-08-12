from collections import Counter

def most_repetitive_word(filename):
    with open(filename) as f:
        words = f.read().split()
        count = Counter(words)
        return count.most_common(1)[0][0]

print(most_repetitive_word("sample.txt"))

