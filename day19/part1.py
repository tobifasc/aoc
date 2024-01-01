inp = open("input", "r").read().strip()

def find_next(wf, part):
    wf_parts = wf.split(",")
    for i, rule in enumerate(wf_parts):
        if i == (len(wf_parts) - 1):
            # we are at the default case - return it
            return rule
        else:
            rule, goal = rule.split(":")
            if "<" in rule:
                prop, val = rule.split("<")
                if part[prop] < int(val):
                    return goal
            if ">" in rule:
                prop, val = rule.split(">")
                if part[prop] > int(val):
                    return goal

workflows, p = inp.split("\n\n")
wf_dict = {}
for workflow in workflows.split("\n"):
    name, rest = workflow.split("{")
    wf_dict[name] = rest[:-1]

parts = []
for part in p.split("\n"):
    part = part[1:-1]
    part_dict = {}
    for prop in part.split(","):
        part_dict[prop[0]] = int(prop[2:])
    parts.append(part_dict)

result = 0
for part in parts:
    wf = 'in'
    while wf != 'A' and wf != 'R':
        wf = find_next(wf_dict[wf], part)
    if wf == "A":
        result += sum(part.values())

print(f"result: {result}")
