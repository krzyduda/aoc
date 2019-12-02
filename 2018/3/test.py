# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 20:01:16 2018

@author: krzyd
"""

class Claim:
    def __init__(self, line):
        parts = line.split()
        cordpart = parts[2][:-1].split(",")
        sizepart = parts[3].split("x")
        self.id = int(parts[0])
        self.topx = int(cordpart[0])
        self.topy = int(cordpart[1])
        self.sizex = int(sizepart[0])
        self.sizey = int(sizepart[1])

class Fabric:
    def __init__(self):
        self.i = 1

def find():
    with open("input.txt") as fp:
        fabric = Fabric()
        for line in fp:
            claim = Claim(line[1:-1])
            fabric.add(claim)
            print(claim)

find()

