#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 02:11:30 2020

@author: jhhalls
"""
# =============================================================================
# Write a Python program which accepts a sequence of comma-separated numbers 
# from user and generate a list and a tuple with those numbers.
# 
# 
# 
# 
# 
# =============================================================================

enter=input('Enter numbers: ')
list=enter.split(',')
tuple = tuple(list)
print('tuple:', tuple)
print('list:', list)

