elves = [x.strip() for x in open("day1-data.txt").read().split("\n\n")]
elfInts = [sum([int(x) for x in e.split("\n")]) for e in elves] 
elfInts.sort()
print(sum(elfInts[-3:]))

# text = open("day1-data.txt").read()
# elves = text.split("\n\n")

# cals = []
# for elf in elves:
#     items = [int(i) for i in elf.split("\n")]
#     cal_sum = sum(items)
#     cals.append(cal_sum)

# print(max(cals))
# print(sum(sorted(cals)[-3:]))