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
        if letter in string.digits:
            mappy[(row, col)] = letter
        elif letter == "*":
            mappy[(row, col)] = "*"
        else:
            mappy[(row, col)] = "."

result = 0
cur_line = 0
cur_num = ""
has_star = False
cur_star_coords = []
gear_map = {}
last_num = ""
for coord, letter in mappy.items():
    if letter in string.digits:
        if cur_line == coord[0]:
            cur_num += letter
        else:
            cur_line = coord[0]
            if len(cur_num) > 0 and has_star:
                for star_coord in cur_star_coords:
                    if star_coord in gear_map:
                        gear_map[star_coord].append(cur_num)
                    else:
                        gear_map[star_coord] = [cur_num]
                has_star = False
            cur_star_coords = []
            cur_num = letter
        for dx, dy in dirs:
            if 0 <= (coord[0] + dy) < max_row and 0 <= (coord[1] + dx) < max_col:
                if mappy[(coord[0] + dy, coord[1] + dx)] == "*":
                    has_star = True
                    cur_star_coord = (coord[0] + dy, coord[1] + dx)
                    if cur_star_coord not in cur_star_coords:
                        cur_star_coords.append(cur_star_coord)

    else:
        cur_line = coord[0]
        if len(cur_num) > 0 and has_star:
            for star_coord in cur_star_coords:
                if star_coord in gear_map:
                    gear_map[star_coord].append(cur_num)
                else:
                    gear_map[star_coord] = [cur_num]
            has_star = False
        cur_num = ""
        cur_star_coords = []

for coord, nums in gear_map.items():
    if len(nums) == 2:
        result += (int(nums[0]) * int(nums[1]))
        print(f"coords: {coord}, nums: {nums}")

print(result)



