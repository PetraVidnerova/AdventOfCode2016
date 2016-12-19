num_elfes =  3017957
#num_elfes = 5

elfes = list(range(1, num_elfes + 1))

even = True

while len(elfes) > 1: 

    #print(elfes)
    if len(elfes) % 2 == 0:
        new_even = even
    else:
        new_even = not even 

    if even:
        elfes = elfes[0::2]
    else:
        elfes = elfes[1::2] 
    even = new_even


print(elfes)

