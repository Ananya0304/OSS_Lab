def file_stats(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)
        num_chars = sum(len(line) for line in lines)
    return num_chars, num_words, num_lines

# Example usage
chars, words, lines = file_stats('example.txt')
print(f"Characters: {chars}, Words: {words}, Lines: {lines}")
