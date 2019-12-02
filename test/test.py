# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 20:01:16 2018

@author: krzyd
"""

def captcha(elements):
    suma = 0
    length = len(elements)
    elements.append(elements[0])
    for i, e in enumerate(elements):
        if i == length:
            return suma
        if e == elements[i+1]:
            suma += int(e)
    return suma

file = open("input.txt","r")

input = file.read()
code = [i for i in input]

print(code)

result = captcha(code)

print(result)

