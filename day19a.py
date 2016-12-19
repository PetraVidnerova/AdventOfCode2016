
#num_elfes =  3017957
num_elfes = 5 

elfes = [1] * num_elfes
elfes = list(enumerate(elfes))

def legth(elfes):
    

while len(elfes) > 1:
    i = 0
    print(elfes)

    while  i < len(elfes):
        
        if elfes[i][1] == 0:
            i += 1
            continue 

        half = length(elfes) // 2
        j = i + half

        if j < len(elfes):
            elfes[j] = (elfes[j][0], 0)
        else:
            j -= len(elfes)
            k, l = 0, 0
            while k < j:
                if elfes[l][1] != 0:
                    k += 1
                l += 1
            elfes[l] = (elfes[l][0], 0)
        i += 1

    elfes = list(filter(lambda x: x[1] != 0, elfes))
        
print(elfes)


