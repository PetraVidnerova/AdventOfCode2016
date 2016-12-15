import copy
import itertools 
import numpy as np

#substances = [ 'H', 'L' ]
#objects = [ 'HM', 'LM', 'HG', 'LG' ]
#index = { 'HM': 1, 'LM' : 2, 'HG' : 3, 'LG' : 4 } 
#couples = [ ('HM', 'LM'), ('HM', 'HG'), ('HM', 'LG'),
#            ('LM', 'HG'), ('LM', 'LG'),
#            ('HG', 'LG') ]
#initial_state = np.array([0, 0, 0, 1, 2], dtype=np.uint8)


substances = [ 'S', 'P', 'T', 'R', 'C' ]
objects = [ 'SM', 'PM', 'TM', 'RM', 'CM', 'SG', 'PG', 'TG', 'RG', 'CG']
index = { 'SM' : 1, 'PM' : 2, 'TM' : 3, 'RM' : 4, 'CM' : 5, 'SG' : 6, 'PG' : 7, 'TG' : 8, 'RG' : 9, 'CG' : 10 } 
couples = list(itertools.combinations(objects, 2))

initial_state = np.array([0, 0, 0,  2, 1, 1, 0, 0, 1, 1, 1], dtype=np.uint8)

UP = 1
DOWN = -1



def elevator(state):
    return state[0] 

def state_print(state): 
    for i in range(4):
        for o in objects:
            if state[index[o]] == i:
                print(o, end=" ")
            else:
                print(". ",end=" ")
        print()
            
def contains(state, what):
    return state[index[what]] == elevator(state) 


def move(state, direction, what, what2=None):
    if state[index[what]] != elevator(state):
        return False # move not possible
    if what2 and state[index[what2]] != elevator(state):
        return False # move not possible

    if elevator(state) == 0 and direction == DOWN:
        return False 
    if elevator(state) == 3 and direction == UP:
        return False 

    state[0] += direction
    state[index[what]] += direction 
    if what2:
        state[index[what2]] += direction
    return True


def fires(state):
    gen_start = 1 + (len(state)-1) // 2 
    floor_safe = [True] * 4 
    for x in state[gen_start:]:   #go through generators 
        floor_safe[x] = False 
    
    # go through chips 
    for i, x in enumerate(state[1:gen_start]):
        if floor_safe[x]: # no generator on floor
            continue
        else:
            if x == state[gen_start+i]: # own generator on floor
                continue
            else:
                return True #chip fires 
    return False 
        

def finished(state):
#    return all(state == 3)
    for x in state[1:]:
        if x != 3:
            return False
    return True 


def step(state):
    
    for direction in [ UP, DOWN]:
        #print("direction", direction, state.elevator)
        if direction == UP and elevator(state) == 3:
            continue
        if direction == DOWN and elevator(state) == 0:
            continue
        # move one 
        for o in objects:
            # if o is on the same floor as elevator
            if contains(state, o): #
                next_state = copy.deepcopy(state)
                move(next_state, direction, o)
                if not fires(next_state):
                    yield next_state
        #move two
        for o1, o2 in couples:
            if contains(state, o1) and contains(state, o2):
                next_state = copy.deepcopy(state)
                move(next_state, direction, o1, o2)
                if not fires(next_state):
                    yield next_state



def test():
                        
    state   = states.pop()
    state_print(state) 
    
    for s in step(state):
        state_print(s)
        states.append(s)

    print("----------")
    state  = states.pop()
    state_print(state) 




if __name__ == "__main__": 

    states = [ initial_state ]
    length = 0


    while True:
        print(length, len(states))
        new_states = []
        for state in states: 
            for newstate in step(state):
                if finished(newstate):
                    print(length+1)
                    quit() 
                new_states.append(newstate) 
        states = new_states
        length += 1





    
