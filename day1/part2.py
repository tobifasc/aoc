import string
f = open("input", "r")
lines = f.readlines()
result = 0
nums = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

def find_digit_or_word(line, dir = "l"):
    substr = ""
    if dir == "r":
        line = line[::-1]
    for letter in line:
        if dir == "r":
            substr = letter + substr
        else:
            substr += letter
        for word, digit in nums.items():
            if letter == digit:
                return digit
            elif len(substr) > 2 and substr.find(word) != -1:
                return digit

result = 0
for line in lines:
    first = find_digit_or_word(line)
    last = find_digit_or_word(line, dir="r")
    result += int(first + last)

print(result)
