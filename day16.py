

def step(s):
    b = s[::-1]
    b2 = ""
    for i in range(len(b)):
        if b[i] == '0':
            b2 = b2 + '1'
        else:
            b2 = b2 + '0'
    return s + '0' + b2

def dragon_curve(init, desired_len):

    while len(init) < desired_len:
        init = step(init)
    return init[:desired_len] 
        

def checksum_step(s):
    i = 0
    res = ""
    while i < len(s)-1:
        if s[i] == s[i+1]:
            res = res + "1"
        else:
            res = res + "0"
        i += 2
    return res

def checksum(s):

    sum = checksum_step(s)
    while len(sum) % 2 == 0:
        sum = checksum_step(sum)
    return sum 


if __name__ == "__main__":

    init = "11101000110010100"
    #disklen = 272
    disklen = 35651584
    
    disk = dragon_curve(init, disklen)
    print(checksum(disk))


