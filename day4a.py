import re 

def rotate(s, number):
    news = ''
    for c in s:
        if c == ' ':
            news += ' '
            continue
        newc = ord('a') + (ord(c) - ord('a') + number) % 26
        news = news + chr(newc) 
    return news


def rotate_room(s):
    s = s.strip() 

    pattern = r'([a-z\-].*)-([0-9].*)\[(.*)\]'
    letters, code, check = re.search(pattern, s).groups()

    letters = letters.replace('-',' ')
    return rotate(letters, int(code)), code 


def test():
    print('qzmt-zixmtkozy-ivhz-343[abc]', 
          rotate_room('qzmt-zixmtkozy-ivhz-343[abc]'))



with open("input4.txt") as file:
    for line in file:
        print(rotate_room(line))


        
