def reverse_each_line(filename):
    with open(filename, 'r') as file:
        for line in file:
            print(line.rstrip()[::-1])

# Example usage
reverse_each_line('example.txt')
