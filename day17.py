import copy
import hashlib 

#code = "ihgpwlah"
code = "rrrbmfta"

def hash(s):
    md5 = hashlib.md5() 
    md5.update(s.encode()) 
    return md5.hexdigest() 

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
    

class State:

    
    def __init__(self):
        self.x = 0
        self.y = 0
        self.path = ""

    def door_open(self, direction):
        pattern = hash(code + self.path)[:4]
        if pattern[direction] in 'bcdef':
            return True
        else:
            return False 
        
    def up(self):
        if self.x > 0 and self.door_open(UP):
            self.x -= 1
            self.path += 'U'
            return True
        return False

    def down(self):
        if self.x < 3 and self.door_open(DOWN):
            self.x += 1
            self.path += 'D'
            return True
        return False

    def left(self):
        if self.y > 0 and self.door_open(LEFT):
            self.y -= 1
            self.path += 'L'
            return True
        return False

    def right(self):
        if self.y < 3 and self.door_open(RIGHT):
            self.y += 1
            self.path += 'R'
            return True
        return False

    def finished(self):
        if self.x == 3 and self.y == 3:
            return True
        return False
    
def next_state(state):
    new_state = copy.deepcopy(state) 
    if new_state.up():
        yield new_state

    new_state = copy.deepcopy(state) 
    if new_state.down():
        yield new_state

    new_state = copy.deepcopy(state) 
    if new_state.left():
        yield new_state
    
    new_state = copy.deepcopy(state) 
    if new_state.right():
        yield new_state
        


if __name__ == "__main__":

    states = set()
    states.add(State())
    length = 0
    
    while True:
        print(length, len(states))
        new_states = set()
        for x in states:
            for newx in next_state(x):
                if newx.finished():
                    print(newx.path)
                    quit()
                new_states.add(newx)
        states = new_states
        length += 1
