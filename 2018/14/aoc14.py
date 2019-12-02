# -*- coself.ding: utf-8 -*-
"""
Created on Sun Dec  9 17:54:54 2018

@author: krzyd
"""

import sys
import mmap

class Board():
    def __init__(self):
        self.recipies = [3, 7]
        self.first = 0
        self.second = 1
        sys.stdout.write(str(3))
        sys.stdout.write(str(7))
        
    def last_ten(self, x):
        return [self.recipies[index] for index in range(x, x + 10)]
      
    def update_current(self):
        f = self.recipies[self.first]
        s = self.recipies[self.second]
        size = len(self.recipies)
        self.first = (self.first + f + 1) % size
        self.second = (self.second + s + 1) % size
    
    def add_new(self):
        rsum = self.recipies[self.first] + self.recipies[self.second]
        if rsum >= 10:
            self.recipies.append(1)
            sys.stdout.write(str(1))
        self.recipies.append(rsum % 10)
        sys.stdout.write(str(rsum % 10))
    
    def do_round(self):
        self.add_new()
        self.update_current()
        
    def found(self, f):
        ll = len(self.recipies)
        if ll < 20:
            return 0
        if self.recipies[-5:] == f:
            return ll - 5
        elif self.recipies[-6:-1] == f:
            return ll - 6
        else :
            return 0
        
    def run(self):
        while(1):
            self.do_round()
        return 1

def find():

    f = open('txt.txt')
    s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    print(s.find(b'077201'))


def find2():
    with open("input2.txt") as fp:
        for line in fp:
            parts = deque(line.split())
            check += calc_node(parts)
    return 0


print(find())

