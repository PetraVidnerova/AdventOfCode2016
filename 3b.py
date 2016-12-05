
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
    i = 0
    x, y, z = [0, 0, 0], [0, 0, 0], [0, 0, 0]
    for line in file:
        if i < 3:
            x[i], y[i], z[i] = line.split()
            i += 1 
            
            if i > 2:
                for a in x, y, z:
                    if is_triangle(int(a[0]), int(a[1]), int(a[2])):
                        triangles += 1
                i = 0

print(triangles)
