# Jacks answer

rucksacks = [x.strip() for x in open("day3-data.txt").readlines()]

def calcPriority(item):
	if item.isupper():
		return ord(item) - ord('A') + 27
	else:
		return ord(item) - ord('a') + 1

prioritySum = 0
for sack in rucksacks:
	c1 = set(sack[:len(sack)//2])
	c2 = set(sack[len(sack)//2:])
		
	shared = list(c1.intersection(c2))[0]
	prioritySum += calcPriority(shared)
	
print(prioritySum)  # part 1


badgePrioritySum = 0 
for i in range(0, len(rucksacks), 3):
	group = (rucksacks[i], rucksacks[i+1], rucksacks[i+2])
	badge = list(set(group[0]).intersection(set(group[1])).intersection(set(group[2])))[0]
	
	badgePrioritySum += calcPriority(badge)

print(badgePrioritySum)


# from string import ascii_lowercase, ascii_uppercase

# def get_priority(letter):
#     all_letters = ascii_lowercase +  ascii_uppercase
#     return all_letters.index(letter) + 1

# def part1():
#     with open("day3.txt") as f:
#         for line in f:
#             line = line.strip()
#             h1 = line[0:len(line)//2]
#             h2 = line[len(line)//2:]

#             for letter in h1: 
#                 if letter in h2:
#                     print(get_priority(letter))
#                     total += get_priority(letter)
#                     break

#     print(total)


# def part2():
#     total = 0
#     sacks = []
#     with open("day3.txt") as f:
#         for line in f:
#             sack = line.strip()
#             sacks.append(sack)

#     for i in range(0, len(sacks), 3):
#         for letter in sacks[i]:
#             if letter in sacks[i + 1] and letter in sacks[i + 2]:
#                 total += get_priority(letter)
#                 break

#     print(total)