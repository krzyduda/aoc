# -*- coself.ding: utf-8 -*-
"""
Created on Sun Dec  9 17:54:54 2018

@author: krzyd
"""

class Pots():
    def __init__(self):
        self.patterns = {}
        self.plants = {}
        
    def init(self, initial):
        print("adding initial: ", initial)
        self.initial = initial
        for idx, val in enumerate(initial):
            if (val == '#'):
                self.plants[idx] = val

    def add(self, note):
        print("adding note: ", note)
        parts = note.split()
        pattern = parts[0]
        result = parts[2]
        
        self.patterns[pattern] = result

    def get_state(self, pot):
        state = []
        for i in range(pot-2, pot+3):
            if (i in self.plants):
                state.append('#')
            else:
                state.append('.')
                 
        return ''.join(state)

    def calculate(self):
        return sum(self.plants)
    
    def grow(self):
        min_plant = min(self.plants)
        max_plant = max(self.plants)
        
        new_plants = {}
        
        for i in range(min_plant - 3, max_plant + 3):
            state = self.get_state(i)
            if state in self.patterns:
                new = self.patterns[state]
                if new == '#':
                    new_plants[i] = new
                    
        self.plants = new_plants
        return sum(self.plants)

def find():
    
    with open("input.txt") as fp:
        pots = Pots()
        for line in fp:
            if len(line) > 15:
                parts = line.split()
                pots.init(parts[2])
            else:
                pots.add(line)
                
        for i in range(10001):
            pots.grow()
            
        return pots.calculate()

def find2():
    with open("input2.txt") as fp:
        for line in fp:
            parts = deque(line.split())
            check += calc_node(parts)
    return 0


print(find())

