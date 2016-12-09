
columns = None # list of columns 

with open("input6.txt") as file:
    for line in file:
        line = line.strip()
        if columns is None:
            columns = [] 
            # split word into columns
            for c in line:
                columns.append([c])
            continue
        
        # split word and add letters to columns
        for i, c in enumerate(line):
            columns[i].append(c)


def min(col):
    """ Returns the least frequent character
    in col.
    col .. list of characters
    """
    
    hist = {} 
    for c in col:
        if c in hist:
            hist[c] += 1
        else:
            hist[c] = 1
    min = len(col)+1
    minc = None
    for c, count in hist.items():
        if count < min:
            min = count
            minc = c
    return minc


for col in columns:
    c = min(col)
    print(c, end="")
print()
