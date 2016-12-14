import hashlib 
import re 

salt = "abc"
hashes = [] 

def hash(s):
    md5 = hashlib.md5() 
    md5.update(s.encode()) 
    return md5.hexdigest() 


def produce_md5(number):
    if number < len(hashes):
        return hashes[number]
    if number == len(hashes):
        hashes.append(hash(salt + str(number))) 
    else:
        raise ValueError("skipped number", number) 
    return hashes[-1] 


def find_triple(s): 
    rx = re.search(r'(.)\1{2}',s)  
    if rx:
        return rx.groups()[0]
    else:
        return None
    
def tuple_5(c, s):
    regex = c + '{5}' 
    if re.search(regex, s):
        return True
    else:
        return False 

def is_key(number):
    
    c = find_triple(produce_md5(number))
    if c is None:
        return False 
        
    for i in range(number+1, number+1001):
        if tuple_5(c, produce_md5(i)):
            return True 
    return False 


def find_64keys():

    index = -1
    count = 0
    while count < 64:
        index += 1 
        if is_key(index):
            count +=1 
    return index


if __name__=="__main__":
    salt = "qzyelonm"
    print(find_64keys())


