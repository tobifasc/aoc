f = open("input", "r")

lines = f.readlines()


time = int(''.join(lines[0][5:].strip().split()))
distances = int(''.join(lines[1][10:].strip().split()))
result = 1

count = 0
for speed in range(time):
    distance = speed * (time - speed)
    if distance > distances:
        count += 1

print(f"result: {count}")

