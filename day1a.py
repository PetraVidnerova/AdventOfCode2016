NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

direction = NORTH
x, y = 0, 0
visited = set()


def turn_left():
    global direction

    direction -= 1
    if direction < 0:
        direction = WEST


def turn_right():
    global direction

    direction += 1
    if direction > 3:
        direction = NORTH


def walk(steps=1):
    global x, y, direction

    if direction == NORTH:
        y += steps
    elif direction == SOUTH:
        y -= steps
    elif direction == EAST:
        x += steps
    elif direction == WEST:
        x -= steps
    else:
        print("Wrong direction.")
        quit()


with open("input1.txt") as file:
    input = file.read()
    steps = input.split(",")

for step in steps:
    step = step.strip()

    # rotate right or left
    if step.startswith('R'):
        turn_right()
    elif step.startswith('L'):
        turn_left()
    else:
        print("Wrong prefix.")
        quit()

    # the rest of the string is number of steps to walk
    for i in range(int(step[1:])):
        walk()

        if (x, y) in visited:
            # print the resulting position
            print(x, y)
            print(abs(x) + abs(y))
            quit()
        else:
            visited.add((x, y))
