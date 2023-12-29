import string

lines = open("input", "r").readlines()

result = 0

for line in lines:
    for letter in line:
        if letter in string.digits:
            first = letter
            break
    for letter in line[::-1]:
        if letter in string.digits:
            last = letter
            break
    result += int(first + last)

print(result)
