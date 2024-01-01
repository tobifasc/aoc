import re

inp = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

f = open("input", "r")


#lines = inp.splitlines()
lines = f.readlines()

result = 0

cards = {}

def get_winner_count(game):
    result = 0
    for winner in game[0]:
        if winner in game[1]:
            result += 1
    return result

# fill cards dict
for line in lines:
    groups = re.search(r"Card\s*(\d+):\s*(((\d+)\s*)+)\s*\|\s*(((\d+)\s*)+)", line).groups()
    card_num = int(groups[0])
    winners = list(map(int, groups[1].strip().split()))
    my_nums = list(map(int, groups[4].strip().split()))
    cards[card_num] = [(winners, my_nums)]

# play games

for card_num, games in cards.items():
    for game in games:
        count = get_winner_count(game)
        while count > 0:
            cards[card_num + count].append(cards[card_num + count][0])
            count -= 1

result = 0
for games in cards.values():
    result += len(games)
print(result)


