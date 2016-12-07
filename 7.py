import re

def containsABBA(s):
    """ Returns True if string s contains sequence 
    ABBA (A and B are different characters). False
    otherwise.
    """ 
    a, b, b1, a1 = 'X', 'X', 'X', 'X'
    for c in s:
        a, b, b1, a1 = b, b1, a1, c
        if a == a1 and b == b1 and a != b:
            return True
    return False
    

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
        if containsABBA(outside) and not containsABBA(inside):
            count += 1
    print(count)
