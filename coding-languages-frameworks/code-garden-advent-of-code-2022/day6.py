data = open("day6-data.txt").read().strip()
# bvwbjplbgvbhsrlpgdmjqwftvncz

for i in range(len(data)-4):
    chunk = data[i:i+4]
    if len(set(chunk)) == 4:
        print(chunk)
        print("First start of packet marker found", i+4)
        break

for i in range(len(data)-14):
    chunk = data[i:i+14]
    if len(set(chunk)) == 14:
        print(chunk)
        print("First start of message marker found", i+14)
        break