import re

def remove_parenthesis_area(lst):
    return [re.sub(r"\s*\(.*?\)", "", s) for s in lst]

data = ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
print(remove_parenthesis_area(data))
