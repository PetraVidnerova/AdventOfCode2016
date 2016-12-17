import copy
import hashlib 
import day17

if __name__ == "__main__":

    maze = [ [ (0, ""), (-1, ""), (-1, ""), (-1, "")],
             [ (-1, ""), (-1, ""), (-1, ""), (-1, "")],
             [ (-1, ""), (-1, ""), (-1, ""), (-1, "")],
             [ (-1, ""), (-1, ""), (-1, ""), (-1, "")]]

    states = set()
    states.add( (day17.State(), 0) )
    
    while states:
        state, length = states.pop()
        for s in day17.next_state(state):
            if length + 1 > maze[s.x][s.y][0]:
                maze[s.x][s.y] = (length + 1, s.path)
            if not s.finished():
                states.add((s, length + 1))
                    
    print(maze[3][3])
