import itertools 
import numpy as np



#initial_state = np.array([0, 0, 0, 1, 2], dtype=np.uint8)

initial_state = np.array([0, 0, 0,  2, 1, 1, 0, 0, 1, 1, 1], dtype=np.uint8)

UP = 1
DOWN = -1

combs = list(itertools.combinations(list(range(1, len(initial_state))), 2))




def elevator(state):
    return state[0] 

def contains(state, what):
    return state[index[what]] == elevator(state) 



def fires(state):
    gen_start = 1 + ((len(state)-1) // 2 )
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
    return all(state == 3)



def step(state):
    
    for direction in [ UP, DOWN ]:
        if direction == UP and elevator(state) == 3:
            continue
        if direction == DOWN and elevator(state) == 0:
            continue
        # move one 
        for i, floor in enumerate(state[1:]):
            if floor == elevator(state): # on the same floor as elevator
                next_state = np.copy(state)
                next_state[0] += direction 
                next_state[i+1] += direction 
                if not fires(next_state):
                    yield next_state
        #move two
        for i, j in combs:
            if state[i] == elevator(state) and state[j] == elevator(state):
                next_state = np.copy(state)
                next_state[0] += direction
                next_state[i] += direction
                next_state[j] += direction
                if not fires(next_state):
                    yield next_state

def is_present(x, l):
    for a in l:
        if all(x == a):
            return True
    return False

if __name__ == "__main__": 

    states = [ initial_state ]
    length = 0

    while True:
        print(length, len(states))
        new_states = []
        while states: 
            state = states.pop()
            for newstate in step(state):
                if finished(newstate):
                    print(length+1)
                    quit() 
                if not is_present(newstate, new_states):                        
                    new_states.append(newstate) 
        states = new_states
        length += 1





    
