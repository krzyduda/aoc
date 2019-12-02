# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 20:01:16 2018

@author: krzyd
"""

class Cord:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sum = 0
        self.infinite = 0
        
def distance(cord1, cord2):
    return (abs(cord1.x - cord2.x) + abs(cord1.y - cord2.y))

def find():
    with open("input.txt") as fp:
        points = []
        for line in fp:
            parts = line.split(",")
            x = int(parts[0])
            y = int(parts[1])
            points.append(Cord(x, y))

        for x in range(400):
            for y in range(400):
                cord = Cord(x, y)
                dist = 400
                for p in points:
                    cdist = distance(cord, p)
                    if cdist == dist:
                        closest = None
                    elif cdist < dist:
                        closest = p
                        dist = cdist
                if closest is not None:
                    closest.sum += 1
                    if x == 0 or y == 0 or x == 399 or y == 399:
                        closest.infinite = 1
        
        biggest = 0
        for p in points:
            if p.infinite == 0 and p.sum > biggest:
                biggest = p.sum
                
        return biggest
            
print(find())

