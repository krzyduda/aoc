# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 12:48:24 2018

@author: krzyd
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 20:01:16 2018

@author: krzyd
"""

def get_mins_and_date(ss):
    parts = ss[1:-1].split()
    dayss = parts[0]
    times = parts[1].split(":")
    hour = int(times[0])
    mins = int(times[1])
    
    

class Entry:
    def __init__(self, line):
        parts = line.split()
        self.guard = -1
        self.sleep = -1
        self.wake = -1
        if len(parts) == 5:
            self.guard = int(parts[3][1:])
        elif parts[1] == "falls":
            self.sleep = 1
        else:
            self.wake = 1
        self.time = 

class Schedule:
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

