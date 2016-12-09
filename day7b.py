import re

def containsABA(s):
    """
    Return lists of BAB sequences.
    """
    res = [] 
    a, b, a1 = 'X', 'X', 'X' 
    for c in s:
        a, b, a1 = b, a1, c
        if a == a1 and a != b:
            res.append(b + a + b)
    return res
    

def split(s):
    """ Returns strings outside and inside, characters
    ouside square brackets and inside square brackets.
    Groups separated by ' '.
    """
    outside, inside = "", ""
    out = True
    for c in s:
        if c == '[':
            out = False
            outside += ' '
            continue
        if c == ']':
            out = True
            inside += ' ' 
            continue
        if out:
            outside += c
        else:
            inside += c
    return outside, inside
            

with open("input7.txt") as file:
    count = 0
    for line in file:
        line = line.strip() 
        outside, inside = split(line)
        #print(outside, inside, end="")
        babs = containsABA(outside)
        for x in babs:
            if x in inside:
                #print("OK")
                count += 1
                break
        #print()
    print(count)
