# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 10:51:02 2018

@author: krzyd
"""

def parse_imm_and_weak(s):
    l = []
    periodp = s.split(',')
    for p in periodp:
        parts = p.split()
        if len(parts) > 1:
            l.append(parts[2])
        else:
            l.append(parts[0])
    return l

class War():
    def __init__(self, immune, infect):
        self.immune = immune
        self.infect = infect
        
    def is_finished(self):
        return all(self.immune.alive) == False or all(self.infect.alive) == False

class Army():
    def __init__(self, line):
        self.alive = True
        self.imm = None
        self.weak = None
        
        parts = line.split('(')
        
        if len(parts) > 1:
            first = parts[0]
            pparts = parts[1].split(')')
            attack = pparts[1]
            iw = pparts[0].split(';')
            
            if len(iw) > 1:
                self.imm = parse_imm_and_weak(iw[0])
                self.weak = parse_imm_and_weak(iw[1])
            elif 'i' in iw[0][0]:
                self.imm = parse_imm_and_weak(iw[0])
            else:
                self.weak = parse_imm_and_weak(iw[0])
            
        elif len

def find():
    immune = []
    with open("input21.txt") as fp:
        for line in fp:
            immune.append(Army(line))
 
    infect = []
    with open("input22.txt") as fp:
        for line in fp: 
            infect.append(Army(line))

    

def find2():
    with open("input2.txt") as fp:
        for line in fp:
            parts = deque(line.split())
            check += calc_node(parts)
    return 0


print(find())