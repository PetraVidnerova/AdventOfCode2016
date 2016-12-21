import re 
import day21 


def un_rotate_position(s, x):
    s2 = day21.rotate_left(s, 1)
    while day21.rotate_position(s2, x) != s:
        s2 = day21.rotate_left(s2, 1)
    return s2 


if __name__ == "__main__":

    mystring = "fbgdceah"

    lines = [] 
    with open("input21.txt") as f:
        for line in f:
            lines.append(line)
        
    for line in lines[::-1]:

        if line.startswith("swap position"):
            x, y = map(int, re.search(r"swap position ([0-9]+) with position ([0-9]+)", line).groups())
            mystring = day21.swap(mystring, y, x)
            continue 

        if line.startswith("swap letter"):
            a, b = re.search(r"swap letter ([a-z]) with letter ([a-z])", line).groups()
            mystring = day21.swap_letters(mystring, a, b)
            continue 

        if line.startswith("rotate left"):
            x = int(re.search(r"rotate left ([0-9]+) step", line).groups()[0])
            mystring = day21.rotate_right(mystring, x) 
            continue 

        if line.startswith("rotate right"):
            x = int(re.search(r"rotate right ([0-9]+) step", line).groups()[0])
            mystring = day21.rotate_left(mystring, x) 
            continue 

        if line.startswith("rotate based"):
            x = re.search(r"rotate based on position of letter ([a-z])", line).groups()[0]
            mystring = un_rotate_position(mystring, x)
            continue 

        if line.startswith("reverse"):
            x, y  = map(int, re.search(r"reverse positions ([0-9]+) through ([0-9]+)", line).groups())
            mystring = day21.reverse(mystring, x, y)
            continue 

        if line.startswith("move"):
            x, y  = map(int, re.search(r"move position ([0-9]+) to position ([0-9]+)", line).groups())
            mystring = day21.move(mystring, y, x)
            continue 
                
    print(mystring)



