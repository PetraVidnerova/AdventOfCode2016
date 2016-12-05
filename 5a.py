import hashlib 

#input = 'abc'
input = 'reyedfim'

def hash(s):
    md5 = hashlib.md5() 
    md5.update(s.encode()) 
    return md5.hexdigest() 

def seven_digit(s):
    """ If first five digits are zero and the 
    sixth digit is in 0-7, returns the seventh
    digit, else returns None."""

    for i in range(5):
        if s[i] != '0':
            return None, None
    if s[5] >= '0' and s[5] <= '7':
        return s[6], s[5]
    else:
        return None, None 

def find_next_digit(s, i):
    d = None
    while d is None:
        d, index = seven_digit(hash(s + str(i))) 
        i += 1 
    return d, index, i 


password = [None]*8 
start = 0

while None in password:
    d, index, start = find_next_digit(input, start)
    index = int(index)
    if password[index] is None:
        password[index] = d 

print(password) 
for c in password:
    print(c, end="")
print()
