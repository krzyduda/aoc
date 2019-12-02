# -*- coself.ding: utf-8 -*-
"""
Created on Sun Dec  9 17:54:54 2018

@author: krzyd
"""

def copy_dicts(t, f):
    for k in f:
        t[k] = f[k].copy()

def get_turns():
    return ['\\', '/', '+']

def get_roads():
    return ['-', '|', '\\', '/', '+']

def get_carts():
    return ['>', '<', '^', 'v']

def is_road(ch):
    return ch in get_roads()

def is_cart(ch):
    return ch in get_carts()

def is_empty(ch):
    return not (is_road(ch) or is_cart(ch))

def to_road(ch):
    if ch == '>' or ch == '<':
        return '-'
    elif ch == '^' or ch == 'v':
        return '|'

def is_cross(ch):
    return ch == '+'

def is_turn(ch):
    return ch in get_turns()

def get_speed(ch):
    if ch == '>':
        return (1, 0)
    elif ch == '<':
        return (-1, 0)
    elif ch == '^':
        return (0, -1)
    elif ch == 'v':
        return (0, 1)
    else:
        print("wrong speed", ch)

class Mine():  
    def __init__(self):
        self.cart_lines = {}
        self.after_lines = {}
        self.crash = None
        self.carts = 0
        self.crash_x = -1
        self.crash_y = -1
        
    def add_line(self, y):
        self.cart_lines[y] = {}
        self.after_lines[y] = {}
    
    def add_point(self, point):
        self.point_lines[point.y][point.x] = point
    
    def add_cart(self, cart):
        self.cart_lines[cart.y][cart.x] = cart
        self.carts += 1

    def check_colision(self, new_x, new_y, x, y):
        if new_y in self.cart_lines:
            if new_x in self.cart_lines[new_y]:
                if x >= new_x and y >= new_y:
                    return False
                return True
        if new_y in self.after_lines:
            if new_x in self.after_lines[new_y]:
                del self.after_lines[new_y][new_x]
                return True
        return False

    def move(self):
        self.crash_x = -1
        self.crash_y = -1
        clean = {}
        copy_dicts(clean, self.after_lines)
        for y in self.cart_lines:
            for x in self.cart_lines[y]:
                if x == self.crash_x and y == self.crash_y:
                    continue
                cart = self.cart_lines[y][x]
                point = self.point_lines[y][x]
                new_x, new_y = cart.move(point)
                if self.check_colision(new_x, new_y, x, y):
                    print("crash ", new_x, new_y)
                    self.crash_x = new_x
                    self.crash_y = new_y
                    self.carts -= 2
                    print("new carts ", self.carts)
                else:
                    self.after_lines[new_y][new_x] = cart
        
        self.cart_lines = {}
        copy_dicts(self.cart_lines, self.after_lines)
        self.after_lines = clean
        
    def is_finished(self):
        return self.carts == 1
    
    def last_cart(self):
        for y in self.cart_lines:
            for x in self.cart_lines[y]:
                cart = self.cart_lines[y][x]
        return cart.x, cart.y

class Point():
    def __init__(self, x, y, direct):
        self.x = x
        self.y = y
        self.direct = to_road(direct)       

class Cart():
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.direction = speed
        self.next_turn = 'l'

    def turn(self):
        if self.next_turn == 'l':
            if self.direction == '^':
                self.direction = '<'
            elif self.direction == 'v':
                self.direction = '>'
            elif self.direction == '<':
                self.direction = 'v'
            else:
                self.direction = '^'
            self.next_turn = 's'
        elif self.next_turn == 's':
            self.next_turn = 'r'
        else:
            if self.direction == '^':
                self.direction = '>'
            elif self.direction == 'v':
                self.direction = '<'
            elif self.direction == '<':
                self.direction = '^'
            else:
                self.direction = 'v'
            self.next_turn = 'l'

    def change_direction(self, point):
        if point == '/':
            if self.direction == '^':
                self.direction = '>'
            elif self.direction == 'v':
                self.direction = '<'
            elif self.direction == '<':
                self.direction = 'v'
            else:
                self.direction = '^'
        elif point == '\\':
            if self.direction == '^':
                self.direction = '<'
            elif self.direction == 'v':
                self.direction = '>'
            elif self.direction == '<':
                self.direction = '^'
            else:
                self.direction = 'v'
        else:
            self.turn()
        
    def move(self, point):
        if is_turn(point):
            self.change_direction(point)
        speedx, speedy = get_speed(self.direction)
        self.x = self.x + speedx
        self.y = self.y + speedy
        return self.x, self.y

def find():
    mine = Mine()
    with open("input.txt") as fp:
        y = 0
        lines = []
        for line in fp:
            mine.add_line(y)
            lines.append([])
            x = 0
            for ch in line:
                if ch == '\n':
                    continue
                lines[y].append(ch)

                if is_cart(ch):
                    cart = Cart(x, y, ch)
                    mine.add_cart(cart)
                
                x += 1
            y += 1
        
        mine.point_lines = lines
            
        while (mine.is_finished() is False):
            mine.move()
            
        return mine.last_cart()

def find2():
    with open("input2.txt") as fp:
        for line in fp:
            parts = deque(line.split())
            check += calc_node(parts)
    return 0


print(find())

