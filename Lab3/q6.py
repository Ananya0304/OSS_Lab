def double_comma_separated_numbers(s):
    return [int(x.strip()) * 2 for x in s.split(',')]

input_str1 = "123, 456, 222, 145"
input_str2 = "-1, 0, -2, 2, 0, 1"
print(double_comma_separated_numbers(input_str1))
print(double_comma_separated_numbers(input_str2))
