import re
import numpy as np 
import copy

class State:

    def __init__(self):
        
        self.x, self.y = 29, 0 # target data position
        self.used = np.zeros((30, 35))
        self.empty =  np.zeros((30, 35))

    def finished(self):
        if self.x == 0 and self.y == 0:
            return True
        return False

        
state = State()
        
with open("input22.txt") as f:
    for line in f:
        if line.startswith("/dev/grid"):
            x, y, used, empty = re.search(r"/dev/grid/node-x([0-9]+)-y([0-9]+)\s+[0-9]+T\s+([0-9]+)T\s+([0-9]+)T", line).groups()
            x, y, used, empty  = map(int, [x, y, used, empty])
            state.used[x, y] = used
            state.empty[x, y] = empty
                  
def next_state(s):
    for i in range(30):
        for j in range(35):
            snew = copy.deepcopy(s)
            if i>0 and snew.empty[i-1, j] < snew.used[i, j]:
                snew.used[i-1, j] += snew.used[i, j]
                snew.empty[i-1, j] -= snew.used[i, j]
                snew.empty[i, j] += snew.used[i, j]
                snew.used[i, j] = 0
                if snew.x == i and snew.y == j:
                    snew.x = i-1
                yield snew
                
            snew = copy.deepcopy(s)
            if i<29 and snew.empty[i+1, j] < snew.used[i, j]:
                snew.used[i+1, j] += snew.used[i, j]
                snew.empty[i+1, j] -= snew.used[i, j]
                snew.empty[i, j] += snew.used[i, j]
                snew.used[i, j] = 0
                if snew.x == i and snew.y == j:
                    snew.x = i+1
                yield snew
                
            snew = copy.deepcopy(s)
            if j>0 and snew.empty[i, j-1] < snew.used[i, j]:
                snew.used[i, j-1] += snew.used[i, j]
                snew.empty[i, j-1] -= snew.used[i, j]
                snew.empty[i, j] += snew.used[i, j]
                snew.used[i, j] = 0
                if snew.x == i and snew.y == j:
                    snew.y = j-1
                yield snew
                
            snew = copy.deepcopy(s)
            if j<34 and snew.empty[i, j+1] < snew.used[i, j]:
                snew.used[i, j+1] += snew.used[i, j]
                snew.empty[i, j+1] -= snew.used[i, j]
                snew.empty[i, j] += snew.used[i, j]
                snew.used[i, j] = 0
                if snew.x == i and snew.y == j:
                    snew.y = j+1
                yield snew


            
states = set()
states.add(state) 
length = 0

while True:
    print(length, len(states))
    newstates = set()

    for x in states:
        for newx in next_state(x):
            if newx.finished():
                print(length+1)
                quit()
            newstates.add(newx)
                
    states = newstates
    length += 1 
