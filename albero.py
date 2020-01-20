#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 13:55:41 2019

@author: andreaagostini
"""

# n (0...r-1) -> n*2+1 stelline
# n -> (r-1)-n spazi

quanteRighe = int(input())

for riga in range(quanteRighe):
    print(' '*(quanteRighe-1-riga) + '*'*(riga*2+1))
    
for n in range(int(quanteRighe/2)):
    print(' '*(quanteRighe-2) + '***')

    

