# -*- coself.ding: utf-8 -*-
"""
Created on Sun Dec  9 17:54:54 2018

@author: krzyd
"""

sta = '('
end = ')'
div = '|'
w = 'W'
s = 'S'
e = 'E'
n = 'N'

def get_opposite(d):
    if e in d:
        return w
    elif w in d:
        return e
    elif n in d:
        return s
    elif s in d:
        return n

class Room():
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.doors = {}
        
    def enter(self, d, room, r):
        d = get_opposite(d)
        self.doors[d] = room
        if r < self.r:
            self.r = r
            
    def leave(self, room, d):
        self.doors[d] = room

class Maze():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.r = 0
        self.bx = []
        self.by = []
        self.br = []
        self.bi = -1
        self.rooms = {}
        st_room = Room(0, 0, 0)
        self.rooms[0] = {}
        self.rooms[0][0] = st_room
        
    def start_branch(self):
        self.bi += 1
        self.bx.append(self.x)
        self.by.append(self.y)
        self.br.append(self.r)
        
    def continue_branch(self):
        self.x = self.bx[self.bi]
        self.y = self.by[self.bi]
        self.r = self.br[self.bi]
        
    def end_branch(self):
        self.bi -= 1
        self.bx.pop()
        self.by.pop()
        self.br.pop()
        
    def get_furthest(self):
        res = 0
        for x in self.rooms:
            for y in self.rooms[x]:
                room = self.rooms[x][y]
                if room.r > 999:
                    res += 1
        return res
        
    def get_room(self, x, y, r):
        if x not in self.rooms:
            self.rooms[x] = {}
        if y not in self.rooms[x]:
            self.rooms[x][y] = Room(x, y, r)
        return self.rooms[x][y]
        
    def get_next(self, d):
        if n in d:
            return self.x, self.y - 1
        elif s in d:
            return self.x, self.y + 1
        elif w in d:
            return self.x - 1, self.y
        elif e in d:
            return self.x + 1, self.y
    
    def go(self, d):
        self.r += 1
        croom = self.rooms[self.x][self.y]
        x, y = self.get_next(d)
        nroom = self.get_room(x, y, self.r)
        nroom.enter(d, croom, self.r)
        croom.leave(nroom, e)
        self.x = x
        self.y = y
        
    def do(self, d):
        if w in d or e in d or s in d or n in d:
            self.go(d)
        elif sta in d:
            self.start_branch()
        elif end in d:
            self.end_branch()
        elif div in d:
            self.continue_branch()

def find():
    with open("input.txt") as fp:
        for line in fp:
            maze = Maze()
            for c in line:
                maze.do(c)
            print(maze.get_furthest())

def find2():
    with open("input2.txt") as fp:
        for line in fp:
            parts = deque(line.split())
            check += calc_node(parts)
    return 0



print(find())

