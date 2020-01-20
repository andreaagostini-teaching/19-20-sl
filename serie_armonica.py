#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 14:19:31 2019

@author: andreaagostini
"""
import math

def mtof(x):
    return (2 ** ((x-69)/12)) * 440
    
def ftom(x):
    if (x > 0):
        m = 69 + 12 * math.log2(x/440)
        return m
    else:
        print(x, "non è una frequenza")
        return 0

fondamentale = 36
armoniche = 16

fFreq = mtof(fondamentale)

for a in range(1, armoniche):
    hFreq = fFreq * a
    hPitch = ftom(hFreq)
    print(hPitch)
    
    
