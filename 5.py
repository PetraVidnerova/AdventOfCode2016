import hashlib 

#input = 'abc'
input = 'reyedfim'

def hash(s):
    md5 = hashlib.md5() 
    md5.update(s.encode()) 
    return md5.hexdigest() 

def sixth_digit(s):
    """ If first five digits are zero, returns 
    the sixth digit, else returns None."""
    if s[:5] != "00000":
        return None
    return s[5] 

def find_next_digit(s, i):
    d = None
    while d is None:
        d = sixth_digit(hash(s + str(i))) 
        i += 1 
    return d, i 


i = 0
for j in range(8):
    d, i = find_next_digit(input, i)
    print(d, end="")
print() 
