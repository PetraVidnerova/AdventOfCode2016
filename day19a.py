from itertools import compress

num_elves =  3017957
#num_elves = 5

elves = list(range(1, num_elves + 1))

even = True

while len(elves) > 1: 
    
    length = len(elves)
    present = [ True ] * length  
    print(length)
    deleted = 0  # number of elves to skip
    for i in range(len(elves)):
        if not present[i]:
            deleted -= 1
            continue 
        half = length // 2 
        k = i + half + deleted 
        if k >= len(elves):
            k -= len(elves)
        present[k] = False
        length -= 1
        deleted += 1 
        
    elves = list(compress(elves, present))

print(elves)

