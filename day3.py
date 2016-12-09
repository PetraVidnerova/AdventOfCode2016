
def is_triangle(x, y, z):

    if x + y <= z:
        return False 
    if x + z <= y:
        return False 
    if z + y <= x:
        return False

    return True 


with open("input3.txt") as file:

    triangles = 0
    for line in file:
        x, y, z = line.split() 
        if is_triangle(int(x), int(y), int(z)):
            triangles += 1

print(triangles)
