import textwrap

def wrap_lines(filename, width):
    with open(filename, 'r') as file:
        for line in file:
            wrapped = textwrap.wrap(line.rstrip(), width)
            for segment in wrapped:
                print(segment)

# Example usage
wrap_lines('example.txt', 40)
