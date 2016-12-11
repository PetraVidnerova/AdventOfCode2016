import copy
import random

substances = [ 'H', 'L' ]
objects = [ 'HM', 'LM', 'HG', 'LG' ]
couples = [ ('HM', 'LM'), ('HM', 'HG'), ('HM', 'LG'),
            ('LM', 'HG'), ('LM', 'LG'),
            ('HG', 'LG') ]

UP = 1
DOWN = -1

class Floors:

    def __init__(self):

            self.elevator = 0
            self.floors = [set(), set(), set(), set()]
            self.floors[0] = set(['HM', 'LM'])
            self.floors[1] = set(['HG'])
            self.floors[2] = set(['LG'])
            self.floors[3] = set()

    def __str__(self):

        for i in range(4):
            for o in objects:
                if o in self.floors[i]:
                    print(o, end=" ")
                else:
                    print(". ",end=" ")
            print()
        return ""
            
        
    def contains(self, what):
        return what in self.floors[self.elevator] 

    def move(self, direction, what, what2=None):
        self.floors[self.elevator].remove(what)
        if what2:
            self.floors[self.elevator].remove(what2)
        self.elevator += direction
        self.floors[self.elevator].add(what)
        self.floors[self.elevator].add(what2)

    def fires(self):
        for floor in self.floors:
            for s in substances:
                if s+'M' not in floor:
                    continue # chip not present 
                if s+'M' in floor and s+'G' in  floor:
                    continue # chip connected
                for s2 in substances:
                    if s2+'G' in floor:
                        #print("fires")
                        return True # chip fires
        return False
        
    def finished(self):
        if 'HM' in self.floors[3] and 'HG' in self.floors[3] and 'LM' in self.floors[3] and 'LG' in self.floors[3]:
            return True
        else:
            return False 


def step(state):
    
    for direction in [ UP, DOWN]:
        #print("direction", direction, state.elevator)
        if direction == UP and state.elevator == 3:
            continue
        if direction == DOWN and state.elevator == 0:
            continue
        # move one 
        for o in objects:
            #print("object", o)
            if state.contains(o):
                next_state = copy.deepcopy(state)
                #print("move", direction, o)
                next_state.move(direction, o)
                if not next_state.fires():
                    yield next_state
        #move two
        for o1, o2 in couples:
            #print("objects", o1, o2)
            if state.contains(o1) and state.contains(o2):
                next_state = copy.deepcopy(state)
                #print("move", direction, o1, o2)
                next_state.move(direction, o1, o2)
                if not next_state.fires():
                    yield next_state

states = [(Floors(),
           0,
           set([Floors()]))]

def test():
                        
    state, steps  = states.pop()
    print(state) 
    
    for s in step(state):
        print(s)
        states.add((s, steps+1))

    print("----------")
    state , steps = states.pop()
    print(state) 

    
min = None        
while True:

    if len(states) == 0:
        break
    
    state, steps, path = states.pop(random.randint(0, len(states)-1))
    #print(state, steps)
    #print("--->", path)
    
    if min is not None and steps > min:
        continue
    
    for s in step(state):
        if s.finished():
            print(steps+1)
            if min is None or steps+1 < min:
                min = steps + 1
        elif s in path:
            # circle
            continue
        else:
            new_path = path
            new_path.add(s)
            states.append((s, steps+1, new_path)) 
