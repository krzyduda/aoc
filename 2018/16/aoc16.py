# -*- coself.ding: utf-8 -*-
"""
Created on Sun Dec  9 17:54:54 2018

@author: krzyd
"""

def addr(bef, instr):
    after = bef.copy()
    i, a, b, c = instr
    after[c] = after[a] + after[b]
    return after

def addi(bef, instr):
    after = bef.copy()
    i, a, b, c = instr
    after[c] = after[a] + b
    return after

def mulr(bef, instr):
    after = bef.copy()
    i, a, b, c = instr
    after[c] = after[a] * after[b]
    return after

def muli(bef, instr):
    after = bef.copy()
    i, a, b, c = instr
    after[c] = after[a] * b
    return after   

def banr(bef, instr):
    after = bef.copy()
    i, a, b, c = instr
    after[c] = after[a] & after[b]
    return after

def bani(bef, instr):
    after = bef.copy()
    i, a, b, c = instr
    after[c] = after[a] & b
    return after

def borr(bef, instr):
    after = bef.copy()
    i, a, b, c = instr
    after[c] = after[a] | after[b]
    return after

def bori(bef, instr):
    after = bef.copy()
    i, a, b, c = instr
    after[c] = after[a] | b
    return after

def setr(bef, instr):
    after = bef.copy()
    i, a, b, c = instr
    after[c] = after[a]
    return after

def seti(bef, instr):
    after = bef.copy()
    i, a, b, c = instr
    after[c] = a
    return after

def gtir(bef, instr):
    after = bef.copy()
    i, a, b, c = instr
    if a > after[b]:
        after[c] = 1
    else:
        after[c] = 0
    return after

def gtri(bef, instr):
    after = bef.copy()
    i, a, b, c = instr
    if after[a] > b:
        after[c] = 1
    else:
        after[c] = 0
    return after

def gtrr(bef, instr):
    after = bef.copy()
    i, a, b, c = instr
    if after[a] > after[b]:
        after[c] = 1
    else:
        after[c] = 0
    return after

def eqir(bef, instr):
    after = bef.copy()
    i, a, b, c = instr
    if a == after[b]:
        after[c] = 1
    else:
        after[c] = 0
    return after

def eqri(bef, instr):
    after = bef.copy()
    i, a, b, c = instr
    if after[a] == b:
        after[c] = 1
    else:
        after[c] = 0
    return after

def eqrr(bef, instr):
    after = bef.copy()
    i, a, b, c = instr
    if after[a] == after[b]:
        after[c] = 1
    else:
        after[c] = 0
    return after

ops = [addr, addi, mulr, muli, banr, bani, borr, bori, setr ,seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

class Case():
    def __init__(self):
        self.before = None
        self.after = None
        self.instr = None

class Cpu():
    def __init__(self):
        self.reg = 1

def find():
    cpu = Cpu()
    case = None
    cases = []
    with open("input.txt") as fp:
        for line in fp:
            if line.startswith("Before"):
                parts = line[9:-2].split(',')
                bef = [int(x) for x in parts]
                case = Case()
                case.before = bef
            elif line.startswith("After"):
                parts = line[9:-2].split(',')
                aft = [int(x) for x in parts]
                case.after = aft
                cases.append(case)
                case = Case()
            else:
                parts = line.split()
                opts = [int(x) for x in parts]
                case.instr = opts
    
    gcount = 0
    match = {}
    tests = {}
    for i, op in enumerate(ops):
        tests[i] = op 
    
    while(len(match) < 16):
        for case in cases:
            count = 0
            index = -1
            code = case.instr[0]
            for t in tests:
                op = tests[t]
                res = op(case.before, case.instr)
                if res == case.after:
                    count += 1
                    index = t
            if count == 1 and code not in match:
                print("found ", index, code)
                match[code] = tests[index]
                del(tests[index])
    print(match)
    
    with open("input2.txt") as fp:
        before = [0, 0, 0, 0]
        for line in fp:
            parts = line.split()
            instr = [int(x) for x in parts]
            before = match[instr[0]](before, instr)
    
    return before[0]
    

def find2():
    with open("input2.txt") as fp:
        for line in fp:
            parts = deque(line.split())
            check += calc_node(parts)
    return 0



print(find())

