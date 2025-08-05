from collections import Counter

def char_frequency(filename):
    with open(filename, 'r') as file:
        text = file.read()
    freq = Counter(text)
    return freq

def guess_file_type(freq):
    if freq.get('{') or freq.get('}') or freq.get('#include'):
        return "C program file"
    elif freq.get('def') or freq.get('import'):
        return "Python program file"
    else:
        return "Text file"

# Example usage
# freq = char_frequency('example.py')
# print(freq)
# print(guess_file_type(freq))
