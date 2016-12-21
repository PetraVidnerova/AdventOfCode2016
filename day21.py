import re 

def swap(s, x, y):
    if x > y:
        x, y = y, x 
    return s[:x] + s[y] + s[x+1:y] + s[x] + s[y+1:]

def swap_letters(s, a, b):
    s = s.replace(a, '?')
    s = s.replace(b, a)
    s = s.replace('?', b)
    return s 
    

def rotate_left(s, x): 
    x = x % len(s)
    return s[x:] + s[:x]
    
    
def rotate_right(s, x):
    x = x % len(s)
    return s[-x:] + s[:-x]


    
def rotate_position(s, x):
    index = s.find(x)
    if index >= 4:
        index += 1
    index += 1 
    return rotate_right(s, index)

def reverse(s, x, y): 
    span = s[x:y+1]
    return s[:x] + span[::-1] + s[y+1:] 

def move(s, x, y): 
    letter = s[x]
    if y > x:
        return s[:x] + s[x+1:y+1] + letter + s[y+1:]
    else:
        return s[:y] + letter + s[y:x] + s[x+1:]


if __name__ == "__main__":

    mystring = "abcdefgh"

    with open("input21.txt") as f:
        for line in f:
            line = line.strip() 

            if line.startswith("swap position"):
                x, y = map(int, re.search(r"swap position ([0-9]+) with position ([0-9]+)", line).groups())
                mystring = swap(mystring, x, y)
                continue 

            if line.startswith("swap letter"):
                a, b = re.search(r"swap letter ([a-z]) with letter ([a-z])", line).groups()
                mystring = swap_letters(mystring, a, b)
                continue 

            if line.startswith("rotate left"):
                x = int(re.search(r"rotate left ([0-9]+) step", line).groups()[0])
                mystring = rotate_left(mystring, x) 
                continue 

            if line.startswith("rotate right"):
                x = int(re.search(r"rotate right ([0-9]+) step", line).groups()[0])
                mystring = rotate_right(mystring, x) 
                continue 

            if line.startswith("rotate based"):
                x = re.search(r"rotate based on position of letter ([a-z])", line).groups()[0]
                mystring = rotate_position(mystring, x)
                continue 

            if line.startswith("reverse"):
                x, y  = map(int, re.search(r"reverse positions ([0-9]+) through ([0-9]+)", line).groups())
                mystring = reverse(mystring, x, y)
                continue 

            if line.startswith("move"):
                x, y  = map(int, re.search(r"move position ([0-9]+) to position ([0-9]+)", line).groups())
                mystring = move(mystring, x, y)
                continue 
                
    print(mystring)



