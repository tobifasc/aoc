import string

dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

inp = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

f = open("input", "r")


#lines = inp.splitlines()
lines = f.readlines()

mappy = {}

max_row = len(lines)
max_col = len(lines[0])

for row, line in enumerate(lines):
    for col, letter in enumerate(line):
        if letter == "." or letter in string.digits:
            mappy[(row, col)] = letter
        elif letter != "\n":
            mappy[(row, col)] = "*"
        else:
            mappy[(row, col)] = "."

result = 0
cur_line = 0
cur_num = ""
is_rel = False
last_num = ""
for coord, letter in mappy.items():
    if letter in string.digits:
        if cur_line == coord[0]:
            cur_num += letter
        else:
            cur_line = coord[0]
            if len(cur_num) > 0 and is_rel:
                result += int(cur_num)
                is_rel = False
            cur_num = letter
        if not is_rel:
            for dx, dy in dirs:
                if 0 <= (coord[0] + dy) < max_row and 0 <= (coord[1] + dx) < max_col:
                    if mappy[(coord[0] + dy, coord[1] + dx)] == "*":
                        is_rel = True

    else:
        cur_line = coord[0]
        if len(cur_num) > 0 and is_rel:
            result += int(cur_num)
            is_rel = False
        cur_num = ""

print(result)



