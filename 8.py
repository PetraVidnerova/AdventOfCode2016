import numpy as np
import re

screen = np.zeros((6, 50))
#screen = np.zeros((3, 7))

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

def test():    
    global screen 

    rect(3, 2)
    rotate_column(1, 1)
    rotate_row(0, 4)
    rotate_column(1, 1)
    print(screen)


with open("input8.txt") as file:

    for line in file:
        line = line.strip()
        if line.startswith("rect"):
            A, B = re.search(r'rect (.*)x(.*)', line).groups()
            rect(int(A), int(B))

        elif line.startswith("rotate row"):
            row, B = re.search(r'rotate row y=(.*) by (.*)', line).groups()
            rotate_row(int(row), int(B))

        elif line.startswith("rotate column"):
            col, B = re.search(r'rotate column x=(.*) by (.*)', line).groups()
            rotate_column(int(col), int(B))

        else:
            raise Error("parse error: "+line)

print(sum(sum(screen)))

import matplotlib.pyplot as plot
plot.imshow(screen)
plot.show()
