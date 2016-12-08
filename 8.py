import numpy as np

#screen = np.zeros((6, 50))
screen = np.zeros((3, 7))

def rect(A,B):
    global screen 
    screen[:B, :A] = 1

def rotate_row(row, B):
    global screen
    newscreen = screen.copy()
    newscreen[row][:B] = screen[row][-B:]
    newscreen[row][B:] = screen[row][:-B]
    screen = newscreen

def rotate_column(col, B):
    global screen 
    screen = screen.T
    rotate_row(col, B)
    screen = screen.T
    
print(screen)
rect(3, 2)
print(screen)
rotate_column(1, 1)
print(screen)
rotate_row(0, 4)
rotate_column(1, 1)
print()
print(screen)
