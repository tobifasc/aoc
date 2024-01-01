from collections import Counter
from functools import cmp_to_key

f = open("input", "r")

lines = f.readlines()

types = {'high': [], 'one': [], 'two': [], 'three': [], 'full': [], 'four': [], 'five': []}

for line in lines:
    hand, bid = line.strip().split()
    bid = int(bid)
    counted = Counter(hand)
    counts = counted.values()

    if len(counts) == 1:
        types['five'].append((hand, bid))
    elif len(counts) == 2:
        if 'J' in counted:
            types['five'].append((hand, bid))
        elif 4 in counts:
            types['four'].append((hand, bid))
        else:
            types['full'].append((hand, bid))
    elif len(counts) == 3:
        if ('J' in counted and 3 in counts) or ('J' in counted and counted['J'] == 2):
            types['four'].append((hand, bid))
        elif 'J' in counted:
            # AJ7JA
            types['full'].append((hand, bid))
        elif 3 in counts:
            types['three'].append((hand, bid))
        else:
            types['two'].append((hand, bid))
    elif len(counts) == 4:
        if 'J' in counted:
            types['three'].append((hand, bid))
        else:
            types['one'].append((hand, bid))
    else:
        if 'J' in counted:
            types['one'].append((hand, bid))
        else:
            types['high'].append((hand, bid))

strength = 'AKQT98765432J'
def hands_cmp(a, b):
    hand_a = a[0]
    hand_b = b[0]
    for i in range(5):
        cur_a = hand_a[i]
        cur_b = hand_b[i]
        if cur_a == cur_b:
            continue
        elif strength.index(cur_a) > strength.index(cur_b):
            return -1
        else:
            return 1

rank = 1
result = 0
hands_cmp = cmp_to_key(hands_cmp)
for dings, hands in types.items():
    hands.sort(key=hands_cmp)
    
    for hand in hands:
        result += rank * hand[1]
        rank += 1


print(result)


