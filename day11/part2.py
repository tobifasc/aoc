f = open("input", "r")

lines = f.readlines()

lines = list(map(lambda x:x.strip(), lines))

col_len = len(lines[0])
line_len = len(lines)
cols = [''] * col_len

should_double_line = [True] * line_len
should_double_col = [True] * col_len
for i, line in enumerate(lines):
    for j, letter in enumerate(line):
        cols[j] += letter
        if letter != '.':
            should_double_line[i] = False
            should_double_col[j] = False

galaxies = []
for row, line in enumerate(lines):
    for col, letter in enumerate(line):
        if letter != '.':
            galaxies.append((row, col))

def get_path(start, finish):
    min_line = min(start[0], finish[0])
    max_line = max(start[0], finish[0])
    min_col = min(start[1], finish[1])
    max_col = max(start[1], finish[1])

    doublies_line = 0
    doublies_col = 0
    if max_line > (min_line + 1):
        doublies_line = sum([(1000000 - 1) if x else 0 for x in should_double_line[min_line + 1:max_line]])
    if max_col > (min_col + 1):
        doublies_col = sum([(1000000 - 1) if x else 0 for x in should_double_col[min_col + 1:max_col]])

    result = doublies_line + max_line - min_line
    result += doublies_col + max_col - min_col
    return result

result = sum([get_path(galaxies[p1], galaxies[p2]) for p1 in range(len(galaxies)) for p2 in range(p1+1,len(galaxies))])

print(result)

