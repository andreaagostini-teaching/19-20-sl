#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 14:27:38 2019

@author: andreaagostini
"""

import random

#random.seed(5) # inizializza il generatore

if (random.random() < 0.5):
    a = 5
else:
    a = 10
    
print('e adesso conto fino a ', a)

for i in range(a):
    x = random.random()
    print(x)

print('"qui!"')
