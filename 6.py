
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


def max(col):
    """ Returns the most frequent character
    in col.
    col .. list of characters
    """
    
    hist = {} 
    for c in col:
        if c in hist:
            hist[c] += 1
        else:
            hist[c] = 1
    max = 0
    maxc = None
    for c, count in hist.items():
        if count > max:
            max = count
            maxc = c
    return maxc


for col in columns:
    c = max(col)
    print(c, end="")
print()
