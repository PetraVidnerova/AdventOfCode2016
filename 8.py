import numpy as np

#screen = np.zeros((6, 50))
screen = np.zeros((3, 7))

def rect(A,B):
    global screen 
    screen[:B, :A] = 1

def rotate_row(row, B):
    global screen
    screen[row][:B], screen[row][B:] = screen[row][-B:], screen[row][:-B]

def rotate_column(col, B):
    global screen 
    screen = screen.T
    rotate_row(col, B)
    screen = screen.T
    
print(screen)
rect(3, 2)
print(screen)
rotate_row(0, 1)
print(screen)
