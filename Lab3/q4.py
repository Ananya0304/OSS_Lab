from itertools import product

def two_digit_combinations(digits, string_maps):
    if len(digits) < 2:
        return []
    combinations = []
    for i in range(len(digits) - 1):
        first = string_maps.get(digits[i], "")
        second = string_maps.get(digits[i + 1], "")
        combinations.extend([''.join(p) for p in product(first, second)])
    return combinations

string_maps = {
    "1": "abc",
    "2": "def",
    "3": "ghi",
    "4": "jkl",
    "5": "mno",
    "6": "pqrs",
    "7": "tuv",
    "8": "wxy",
    "9": "z"
}

digit_string = "123"
print(two_digit_combinations(digit_string, string_maps))
