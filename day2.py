buttons = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
x, y = 1, 1
code = []


def down():
    global x

    if x < 2:
        x += 1


def up():
    global x

    if x > 0:
        x -= 1


def left():
    global y

    if y > 0:
        y -= 1


def right():
    global y

    if y < 2:
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
