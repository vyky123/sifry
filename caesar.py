#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 12:52:58 2017

@author: vyk35227
"""
vyber = input("Posun v abecedě nebo klíčové slovo? POSUN/KLIC > ").upper() 
    
if vyber == "POSUN":            #posun v abecedě
    n = int(input("Zadej číslo posunu > "))
    m = input("Zadej text > ").upper()
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    b = a[n:] + a[:n]
    f = 0
    

    if " " in m:
        m = m.replace(" ","")
        
    for i in m:
        g = m[f]
        f = f + 1
        x = b[a.index(g)]
        print(x, end="")

else:
    if vyber == "KLIC":                         #pomocí klíčového slova
        m = input("Zadej text > ").upper()
        a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        f = 0       
        x = ""
        sif = input("Šifrovat nebo dešifrovat? Zadej SIF/DES > ").upper()  
        
           
        if sif == "SIF":                        #šifrování
            n = input("Zadej klíč > ").upper() 
            
            for i in m:
                cislo = a.find(i)
                f = 0
                cislo = cislo + ( (ord(n[f])) - ord("A") )
                f = f + 1
                f = f % len(n)
                if cislo >= len(a):
                    cislo = cislo - len(a)
                        
                x = x + a[cislo]
        
        else:
            if sif == "DES":                    #dešifrování
                n = input("Zadej klíč > ").upper() 
                for i in m:
                    cislo = a.find(i)
                    f = 0
                    cislo = cislo - ((ord(n[f])) - ord("A") )
                    f = f + 1
                    f = f % len(n)
                    if cislo >= len(a):
                        cislo = cislo - len(a)
                            
                    x = x + a[cislo]
            else:
                print("Odpověď musí být SIF/DES")
        print(x)
    else:
        print("Odpověď musí být POSUN/KLIC")
            