
def make_first_row(s):
    row = [] 
    for x in s:
        if x == '.':
            row.append(True)
        else:
            row.append(False)
    return row

def is_safe(row, index):
    if index < 0 or index >= len(row):
        return True
    return row[index]

def make_next_row(row):
    next_row = [] 
    for i in range(len(row)):
        if is_safe(row, i-1) == is_safe(row, i) and is_safe(row, i) != is_safe(row, i+1):
            next_row.append(False)
            continue
        if is_safe(row, i+1) == is_safe(row, i) and is_safe(row, i) != is_safe(row, i-1):
            next_row.append(False)
            continue
        next_row.append(True)
    return next_row



if __name__ == "__main__":

    row = make_first_row(".^^^.^.^^^.^.......^^.^^^^.^^^^..^^^^^.^.^^^..^^.^.^^..^.^..^^...^.^^.^^^...^^.^.^^^..^^^^.....^....")
    count = sum(row)
    for i in range(1, 400000):
        row = make_next_row(row)
        count += sum(row)
    print(count)
