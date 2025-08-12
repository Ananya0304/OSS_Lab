with open("file1.txt", "w") as f1:
    f1.write("Hello World")

with open("file2.txt", "w") as f2:
    f2.write("Python is fun")

def extract_characters(filenames):
    characters = []
    for filename in filenames:
        with open(filename, "r") as f:
            characters.extend(list(f.read()))
    return characters

files = ["file1.txt", "file2.txt"]
print(extract_characters(files))
