buttons = [['x', 'x', 1, 'x', 'x'],
           ['x', 2, 3, 4, 'x'],
           [5, 6, 7, 8, 9],
           ['x', 'A', 'B', 'C', 'x'],
           ['x', 'x', 'D', 'x', 'x']]
x, y = 2, 0
code = []


def border_left(x, y):
    if y == 0:
        return True
    if y == 1 and (x == 1 or x == 3):
        return True
    if y == 2 and (x == 0 or x == 4):
        return True
    return False


def border_right(x, y):
    if y == 2 and (x == 0 or x == 4):
        return True
    if y == 3 and (x == 1 or x == 3):
        return True
    if y == 4:
        return True
    return False


def border_up(x, y):
    if x == 0:
        return True
    if x == 1 and (y == 1 or y == 3):
        return True
    if x == 2 and (y == 0 or y == 4):
        return True
    return False


def border_down(x, y):
    if x == 2 and (y == 0 or y == 4):
        return True
    if x == 3 and (y == 1 or y == 3):
        return True
    if x == 4:
        return True
    return False


def down():
    global x, y

    if not border_down(x, y):
        x += 1


def up():
    global x, y

    if not border_up(x, y):
        x -= 1


def left():
    global x, y

    if not border_left(x, y):
        y -= 1


def right():
    global x, y

    if not border_right(x, y):
        y += 1


with open("input2.txt") as file:

    for line in file:
        line = line.strip()
        # go through line and move
        for c in line:
            if c == "U":
                up()
            elif c == "D":
                down()
            elif c == "R":
                right()
            elif c == "L":
                left()
            else:
                print("Wrong direction", c)
                quit()
        # append letter
        code.append(buttons[x][y])

print(code)
