import re 

def first_max(list):
    """ Takes a list of couples (letter, count), 
    returns the first one with max count. """ 
    max = 0
    letter = None
    for l, count  in list:
        if count > max:
            max = count 
            letter = l 
    return letter, max 

def get_five_most(s):
    s = sorted(s) 

    # make a sorted list of (letter, count)
    lastc = None
    count = 0
    hist = [] 
    s.append('X')
    for c in s:
        if c == lastc:
            count += 1 
        else:
            if lastc is not None:
                hist.append((lastc, count))
            lastc = c 
            count = 1
    hist = sorted(hist)

    res = [] 
    for i in range(5):
        l, c = first_max(hist)
        hist.remove((l, c)) 
        res.append(l) 

    return res
            

def is_room(s):
    s = s.strip() 

    pattern = r'([a-z\-].*)-([0-9].*)\[(.*)\]'
    letters, code, check = re.search(pattern, s).groups()

    code = int(code)
    letters = letters.replace('-','')
    five_most = sorted(get_five_most(letters))
    check = sorted(check)
    
    if five_most == check:
        return code 

    return 0

def test():
    vals = ['aaaaa-bbb-z-y-x-123[abxyz]',
            'a-b-c-d-e-f-g-h-987[abcde]',
            'not-a-real-room-404[oarel]',
            'totally-real-room-200[decoy]'] 

    for val in vals:
        print(val, is_room(val))



sum = 0
with open("input4.txt") as file:
    for line in file:
        sum += is_room(line)

print(sum)
        
