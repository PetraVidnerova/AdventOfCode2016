from itertools import compress

num_elves =  3017957
#num_elves = 5

elves = list(range(1, num_elves + 1))

even = True

while len(elves) > 1: 
    
    length = len(elves)
    print(length)
    present = [ True ] * length  
    for i in range(len(elves)):
        if not present[i]:
            continue 
        half = length // 2 
        j = i + half
        k = i  
        while j > 0:
            k += 1 
            if k >= len(elves):
                k -= len(elves)
            if present[k]: 
                j -= 1
        present[k] = False
        length -= 1 
    
    elves = list(compress(elves, present))

print(elves)

