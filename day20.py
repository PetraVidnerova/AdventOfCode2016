import numpy as np


blacklist = []

with open("input20.txt") as f:
    for line in f:
        vals = list(map(int, line.split('-')))
        blacklist.append((vals[0], vals[1]))

blacklist = sorted(blacklist)

ip = 0
i = 0

while i < len(blacklist):
    
    if blacklist[i][0] <= ip <= blacklist[i][1]:
        ip = blacklist[i][1] + 1
        i = 0
        continue
        
    i += 1

print(ip)
