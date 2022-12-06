import re

with open("day5-data.txt") as f:
    text = f.read()
    initial , moves = text.split("\n\n")
    moves = moves.split("\n")
    move_tuples = []
    for move in moves:
        x = re.search("move (\d+) from (\d+) to (\d+)", move)
        move_tuples.append((int(x[1]), int(x[2]), int(x[3])))

    print(initial)

    stack_indexes = {i: 4 * (i - 1) + 1 for i in range(1,10)}
    stacks = {i: [] for i in stack_indexes}

    for row in initial.split("\n"):
        if "1" not in row:
            for l, i in stack_indexes.items():
                if row[i] != " ":
                    stacks[l].append(row[i])


print(stacks)
for num, start, fin in move_tuples:
    # for i in range(num):
        slice1 = stacks[start][:num]
        print(slice1)
        remaining = stacks[start][num:]
        stacks[start] = remaining
        stacks[fin] = slice1 + stacks[fin]

print(stacks)

# print("".join([v[0] for v in stacks.values() if len(v)>0]))

print()
print()
print(stacks.values())

print()
for v in stacks.values():
    # if len(v) > 0:
        print(v[0], end="")
    