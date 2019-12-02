# -*- coself.ding: utf-8 -*-
"""
Created on Sun Dec  9 17:54:54 2018

@author: krzyd
"""

def addr(bef, instr):
    after = bef.copy()
    a, b, c = instr
    after[c] = after[a] + after[b]
    return after

def addi(bef, instr):
    after = bef.copy()
    a, b, c = instr
    after[c] = after[a] + b
    return after

def mulr(bef, instr):
    after = bef.copy()
    a, b, c = instr
    after[c] = after[a] * after[b]
    return after

def muli(bef, instr):
    after = bef.copy()
    a, b, c = instr
    after[c] = after[a] * b
    return after   

def banr(bef, instr):
    after = bef.copy()
    a, b, c = instr
    after[c] = after[a] & after[b]
    return after

def bani(bef, instr):
    after = bef.copy()
    a, b, c = instr
    after[c] = after[a] & b
    return after

def borr(bef, instr):
    after = bef.copy()
    a, b, c = instr
    after[c] = after[a] | after[b]
    return after

def bori(bef, instr):
    after = bef.copy()
    a, b, c = instr
    after[c] = after[a] | b
    return after

def setr(bef, instr):
    after = bef.copy()
    a, b, c = instr
    after[c] = after[a]
    return after

def seti(bef, instr):
    after = bef.copy()
    a, b, c = instr
    after[c] = a
    return after

def gtir(bef, instr):
    after = bef.copy()
    a, b, c = instr
    if a > after[b]:
        after[c] = 1
    else:
        after[c] = 0
    return after

def gtri(bef, instr):
    after = bef.copy()
    a, b, c = instr
    if after[a] > b:
        after[c] = 1
    else:
        after[c] = 0
    return after

def gtrr(bef, instr):
    after = bef.copy()
    a, b, c = instr
    if after[a] > after[b]:
        after[c] = 1
    else:
        after[c] = 0
    return after

def eqir(bef, instr):
    after = bef.copy()
    a, b, c = instr
    if a == after[b]:
        after[c] = 1
    else:
        after[c] = 0
    return after

def eqri(bef, instr):
    after = bef.copy()
    a, b, c = instr
    if after[a] == b:
        after[c] = 1
    else:
        after[c] = 0
    return after

def eqrr(bef, instr):
    after = bef.copy()
    a, b, c = instr
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
        self.instr = []
        self.ipr = -1
        self.ip = 0
        self.reg = [0, 0, 0, 0, 0, 0]
        self.ops = {}
        for f in ops:
            self.ops[f.__name__] = f
        
    def add_instr(self, instr):
        #print("add instr ", instr.op, instr.args)
        self.instr.append(instr)
        
    def set_ip(self, ip):
        #print("ip to ", ip)
        self.ipr = ip
        self.ip = self.reg[ip]
        
    def run(self, instr):
        #print("before: ", self.reg)
        after = self.ops[instr.op](self.reg, instr.args)
        self.reg = after
        #print("after: ", self.reg)
        
    def execute(self):
        print("executing")
        count = 0
        done1 = 0
        done2 = 0
        while(self.ip < len(self.instr)):
            self.reg[self.ipr] = self.ip
            
            ins = self.instr[self.ip]
            #print("running: ", ins.op, ins.args)
            self.run(ins)
            
            self.ip = self.reg[self.ipr]
            self.ip += 1
            #print("ip set to ", self.ip)

            count += 2

class Instr():
    def __init__(self, op, args):
        self.op = op
        self.args = args

def find():
    cpu = Cpu()
    with open("input.txt") as fp:
        for line in fp:
            parts = line.split()
            if len(parts) == 2:
                cpu.set_ip(int(parts[1]))
            elif len(parts) == 4:
                inst = Instr(parts[0], [int(x) for x in parts[1:]])
                cpu.add_instr(inst)
    
    cpu.execute()
    
    return cpu.reg[0]
    

def find2():
    with open("input2.txt") as fp:
        for line in fp:
            parts = deque(line.split())
            check += calc_node(parts)
    return 0



print(find())

