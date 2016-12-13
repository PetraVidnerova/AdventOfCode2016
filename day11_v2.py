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
        if self.elevator == 0 and direction == DOWN:
            raise Exception()
        if self.elevator == 3 and direction == UP:
            raise Exception()
        
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

def first_edge():
    return (UP, objects[0], None)

def next_item(x, l):
    for i in range(len(l)-1):
        if x == l[i]:
            return l[i+1]
    assert(x == l[-1])
    return None

def next_edge(edge):
    direction, o1, o2 = edge
    
    if o2 is None:
        no1 = next_item(o1, objects)
        if no1 is None:
            no1, no2 = couples[0]
            return direction, no1, no2
        return direction, no1, None
    else:
        no1_no2 = next_item((o1,o2), couples)
        if no1_no2 is None and direction == DOWN:
            return None
        elif no1_no2 is None and direction == UP:
            return DOWN, objects[0], None
        else:
            return direction, no1_no2[0], no1_no2[1] 
                

def test_edges():
    e = first_edge()
    print(e)
    while e is not None:
        e = next_edge(e)
        print(e)
        

def test():
                        
    state, steps  = states.pop()
    print(state) 
    
    for s in step(state):
        print(s)
        states.add((s, steps+1))

    print("----------")
    state , steps = states.pop()
    print(state) 




class Stack:

    stack = [ ]

    def pop(self):
        state, edge = self.stack.pop()
        return edge 

    def add(self, state, edge):
        self.stack.append((state, edge))

    def length(self):
        return len(self.stack)

    def active_state(self):
        return self.stack[-1][0] 

    def contains_state(self, state):
        for s, e in self.stack:
            if s == state:
                return True
        return False

    
stack = Stack()
stack.add( Floors(), None )

edge = None
while True:
    #print(stack.length())
    state = stack.active_state()
    if edge is None:
        edge = first_edge()
    else:
        edge = next_edge(edge)
    if edge is None:
        #print("coufcouf")
        # toz couvnem
        edge = stack.pop()
        if edge is None:
            break
        continue
    else:
        #print("move", edge)
        #create new state
        new_state = copy.deepcopy(state)
        try:
            new_state.move(*edge)
        except KeyError:
            # move is not possible
            continue
        except Exception:
            # move is not possible 
            continue
        # if state is already in path, continue
        if stack.contains_state(new_state):
            continue
        # if the state is correct add it to stack
        if stack.length() < 12 and not new_state.fires():
            if new_state.finished():
                print("--->", stack.length())
                continue
            #print("move successful")
            stack.add(new_state, edge)
            edge = None 
