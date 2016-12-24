import re
import itertools

grid = [] 

with open("input22.txt") as f:
    for line in f:
        if line.startswith("/dev/grid"):
            x, y = re.search(r"/dev/grid/node-x[0-9]+-y[0-9]+\s+[0-9]+T\s+([0-9]+)T\s+([0-9]+)T", line).groups()
            x, y = map(int, [x, y])
            grid.append((x, y))
                  

count = 0
for a, b in itertools.combinations(grid, 2):
    if a[0] != 0 and a[0] <= b[1]:
        count += 1
    if b[0] != 0 and b[0] <= a[1]:
        count += 1
      
            
print(count)
