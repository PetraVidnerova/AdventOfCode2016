from bitarray import bitarray 

blacklist = bitarray(4294967295)
blacklist.setall(True)

with open("input20.txt") as f:
    for line in f:
        line = line.strip()
        print(line)
        vals = list(map(int, line.split('-')))
        blacklist[vals[0]:vals[1]+1] = False


print("ready")
print(sum(blacklist))
