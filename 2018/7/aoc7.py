# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 20:01:16 2018

@author: krzyd
"""

def get_characters():
    return []

class Step:
    def __init__(self, id):
        self.id = id
        
    def add_preq(self, id):
        self.id = id

def find():
    steps = {}
    pre = {}
    post = {}
    characters = [chr(x) for x in range(65, 91)]
    for ch in characters:
        steps[ch] = ch
        pre[ch] = []
        post[ch] = []
    with open("input.txt") as fp:
        for line in fp:
            parts = line.split()
            before = parts[1]
            after = parts[7]
            pre[after].append(before)
            post[before].append(after)
    
    order = []
    
    while (len(characters) > 0):
        for ch in characters:
            if len(pre[ch]) == 0:
                for p in post[ch]:
                    pre[p].remove(ch)
                order.append(ch)
                characters.remove(ch)
                break
    
    return ''.join(order)

def cost(ch):
    return 61 + (ord(ch) - 65)

def find2():
    steps = {}
    pre = {}
    post = {}
    
    characters = [chr(x) for x in range(65, 91)]
    workers = 5
    for ch in characters:
        steps[ch] = ch
        pre[ch] = []
        post[ch] = []
    with open("input.txt") as fp:
        for line in fp:
            parts = line.split()
            before = parts[1]
            after = parts[7]
            pre[after].append(before)
            post[before].append(after)
    
    order = []
    second = 0
    ready = {}
    for i in range(10000):
        ready[i] = []
    
    while (len(characters) > 0 or
           (len(characters) == 0 and workers < 5)):
        print("second ", second)
        for x in ready[second]:
            for p in post[x]:
                pre[p].remove(x)
            order.append(p)
            workers += 1
            print("ready: ", x)

        for ch in characters:
            if (len(pre[ch]) == 0) and workers > 0:
                characters.remove(ch)
                workers -= 1
                ready[second + cost(ch)].append(ch)
                print("starting ", ch)
    
        second += 1
    
    return second-1

print(find2())

