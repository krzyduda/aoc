# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 20:01:16 2018

@author: krzyd
"""
from collections import deque

def calc_node(elements):
    node_sum = 0
    nodes = {}
    meta_sum = 0
    
    n_child = int(elements.popleft())
        
    n_meta = int(elements.popleft())
    
    for i in range(1, n_child+1):
        nodes[i] = calc_node(elements)
    
    for i in range(n_meta):
        meta = elements.popleft()
        meta_val = int(meta)
        meta_sum += meta_val
        if meta_val in nodes:
            node_sum += nodes[meta_val]
    
    if n_child == 0:
        return meta_sum
    else:
        return node_sum

def read_node(elements):
    check = 0
    
    if len(elements) == 0:
        return check
    
    n_child = int(elements.popleft())
        
    n_meta = int(elements.popleft())
    
    for i in range(n_child):
        check += read_node(elements)
    
    for i in range(n_meta):
        check += int(elements.popleft())
    
    return check

def find():
    check = 0
    with open("input.txt") as fp:
        for line in fp:
            parts = deque(line.split())
            check += read_node(parts)
    return check

def find2():
    check = 0
    with open("input.txt") as fp:
        for line in fp:
            parts = deque(line.split())
            check += calc_node(parts)
    return check


print(find2())

