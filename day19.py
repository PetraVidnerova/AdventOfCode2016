
num_elfes =  3017957
elfes = [ 1 ] * num_elfes 
elfes = list(enumerate(elfes)) 


while len(elfes) > 1:

    for i in range(len(elfes)-1):
        if elfes[i][1] == 0:
            continue 
        elfes[i+1] = (elfes[i+1][0], 0)

    if elfes[-1][1] != 0:
        elfes[0] = (elfes[0][0], 0) 

    elfes = list(filter(lambda x: x[1] != 0, elfes))


print(elfes)


