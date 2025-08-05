# Writing to a file
with open('example.txt', 'w') as file:
    file.write("First line of text.\n")
    file.write("Second line of text.\n")
    file.writelines(["Third line.\n", "Fourth line.\n"])

# Reading the entire file
with open('example.txt', 'r') as file:
    content = file.read()
    print("Full content:\n", content)

# Reading line by line
with open('example.txt', 'r') as file:
    first_line = file.readline()
    print("First line:", first_line.strip())
