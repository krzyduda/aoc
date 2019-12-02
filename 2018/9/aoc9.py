# -*- coself.ding: utf-8 -*-
"""
Created on Sun Dec  9 17:54:54 2018

@author: krzyd
"""


# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 20:01:16 2018

@author: krzyd
"""

class Marble():
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class Circle():
    def __init__(self):
        self.current = Marble(0)
        self.current.next = self.current
        self.current.prev = self.current
        self.last_used = 0
        
    def insert(self, value):
        marble = Marble(value)
        left = self.current.next
        right = self.current.next.next
        
        left.next = marble
        right.prev = marble
        
        marble.prev = left
        marble.next = right
        
        self.current = marble
        
        return 0
        
    def remove(self):
        
        left = self.current.prev.prev.prev.prev.prev.prev.prev.prev
        right = self.current.prev.prev.prev.prev.prev.prev
        
        gone = left.next
        left.next = right
        right.prev = left
        self.current = right
        
        return gone.value
        
    def add(self, value):
        self.last_used = value
        
        if (value % 23) == 0:
            return value + self.remove()
        else:
            return self.insert(value)


class Game():
    def __init__(self, n_players, last_marble):
        self.n_players = n_players
        self.players = [0 for x in range(n_players + 1)]
        self.last_marble = last_marble
        self.circle = Circle()
        
    def increment(self):
        if self.c_player == self.n_players:
            self.c_player = 1
        else:
            self.c_player += 1
        
    def play(self):
        self.c_player = 0
        max_score = 0
        
        for x in range(1, self.last_marble+1):
            score = self.circle.add(x)
            self.players[self.c_player] += score
            if self.players[self.c_player] > max_score:
                max_score = self.players[self.c_player]
            self.increment()
            
        return max_score

def find():
    with open("input3.txt") as fp:
        for line in fp:
            parts = line.split()
            n_players = int(parts[0])
            last_marble = int(parts[6])
            print("players ", n_players)
            print("last marble ", last_marble)
            game = Game(n_players, last_marble)
            score = game.play()
            print("score ", score)
    return score

def find2():
    check = 0
    with open("input.txt") as fp:
        for line in fp:
            parts = deque(line.split())
            check += calc_node(parts)
    return check


print(find())

