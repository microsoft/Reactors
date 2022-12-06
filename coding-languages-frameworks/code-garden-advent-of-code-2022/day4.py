
pairRanges = [x.strip().split(',') for x in open("data.txt").readlines()]

# Jacks Answer

totalOverlaps = 0
anyOverlaps = 0
for a, b in pairRanges:
	aStart, aStop = a.split('-')
	bStart, bStop = b.split('-')
	
	aRange = set([x for x in range(int(aStart), int(aStop)+1)])
	bRange = set([x for x in range(int(bStart), int(bStop)+1)])
	
	if aRange.issubset(bRange) or bRange.issubset(aRange):
		totalOverlaps += 1

    if len(aRange.intersection(bRange)) != 0:
		anyOverlaps += 1

    print(totalOverlaps)
    print(anyOverlaps)


# Renee's answer
total = 0

with open("day4-data.txt") as f:
    for line in f:
        parts = line.split(",")
        part_ranges = [tuple([int(i) for i in part.split("-")]) for part in parts]
        print(part_ranges)

        
        sorted_ranges = sorted(part_ranges, key=lambda x: (x[0], -x[1]))
        if sorted_ranges[1][1] <= sorted_ranges[0][1]:
            total += 1

        #part
        sorted_ranges = sorted(part_ranges, key=lambda x: (x[0], -x[1]))
            if sorted_ranges[1][0] <= sorted_ranges[0][1]:
                total += 1
