favourite = 10 

def count_bits(x):
    return bin(x).count("1")
        

def maze_is_open(x, y):

    if x < 0 or y < 0:
        return False 

    sum = favourite + x*x + 3*x + 2*x*y + y + y*y
    if count_bits(sum) % 2 == 0:
        return True
    else:
        return False


def next_step(x, y):
    if maze_is_open(x+1, y):
        yield (x+1, y) 
    if maze_is_open(x-1, y):
        yield (x-1, y) 
    if maze_is_open(x, y+1):
        yield (x, y+1) 
    if maze_is_open(x, y-1):
        yield (x, y-1)


def path_len(start, end):
    if start == end:
        return 0  
        
    min = None
    paths = set([ (start, 0) ]) 
    while paths:
        pos, len  = paths.pop() 
        if min is not None and len > min:
            continue 
        for s in next_step(*pos):
            if s == end:
                if min is None or len + 1 < min:
                    min = len + 1 
            else:
                paths.add((s, len+1))
    return min 

def how_many(start):
    paths = set([ (start, 0) ])
    reached = set()
    reached.add(start)
    while paths:
        pos, length = paths.pop() 
        if length >= 50:
            continue 
        for s in next_step(*pos):
            reached.add(s)
            paths.add((s, length+1)) 
    return len(reached)

def test():
    for x in range(10):
        for y in range(10):
            if maze_is_open(y, x):
                print(".", end="")
            else:
                print("#", end="") 
        print() 


if __name__ == "__main__":
    favourite = 1352

    # part 1:
    print(path_len((1, 1), (31, 39)))

    # part 2:
    print(how_many((1,1)))
