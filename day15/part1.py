f = open("input", "r")
inp = f.read().strip()
#inp = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

def calc_val(char, init):
    init += ord(char)
    init *= 17
    return init % 256

result = 0
for val in inp.split(','):
    res = 0
    for letter in val:
        res = calc_val(letter, res)
    result += res

print(result)
