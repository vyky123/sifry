#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 12:52:58 2017

@author: vyk35227
"""
"""
spec = "!@#$%^&*(){}[]\=+-\"~"
n = int(input("Zadej číslo posunu > "))
m = input("Zadej text > ").upper()
a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
b = a[n:] + a[:n]
f = 0
pocet = len(m)

if " " in m:
    m = m.replace(" ","")
    
for i in m:
    g = m[f]
    f = f + 1
    x = b[a.index(g)]
    print(x, end="")
"""


m = input("Zadej text > ").upper()
a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = input("Zadej klíč > ").upper()
f = 0
pocet = len(m)

if " " in m:
    m = m.replace(" ","")
    
for i in n:
    g = n[f]    #písmeno z klíče
    y = y[n.index(g)] #klic[klic.index(pismeno_klic)]
    # pzt = x
    for i in m:
        x = m[f]   #písmeno z textu
        
        f = f + 1
        print(y, end="")
        
