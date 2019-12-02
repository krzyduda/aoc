# -*- coself.ding: utf-8 -*-
"""
Created on Sun Dec  9 17:54:54 2018

@author: krzyd
"""

depth = 3339
targetx = 10
targety = 715

#depth = 510
#targetx = 10
#targety = 10
indices = []
erosions = []

def get_erosion(x, y):
    ind = get_index(x, y)
    return (ind + depth) % 20183

def get_index(x, y):
    if x == 0 and y == 0:
        return 0
    elif x == targetx and y == targety:
        return 0
    elif y == 0:
        return x * 16807
    elif x == 0:
        return y * 48271
    else:
        return erosions[y][x-1] * erosions[y-1][x]

def find():
    result = 0
    for y in range(targety + 1):
        erosions.append([])
        for x in range(targetx + 1):
            erosion = get_erosion(x, y)
            erosions[y].append(erosion)
            result += erosion % 3
    return result

def find2():
    with open("input2.txt") as fp:
        for line in fp:
            parts = deque(line.split())
            check += calc_node(parts)
    return 0




print(find())

