#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 02:32:25 2020

@author: trendydice
"""

# =============================================================================
# 
#  Write a Python program that accepts an integer (n) and
#  computes the value of n+nn+nnn. Go to the editor
#  Sample value of n is 5
#  
# 
# Expected Result : 615
# 
# 
# =============================================================================

n = input('enter n: ')
print(int(n*3) + int(n*2) +int(n))