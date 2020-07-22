#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 02:15:51 2020

@author: trendydice
"""

# =============================================================================
# 7. Write a Python program to accept a filename from the user 
# and print the extension of that.
# =============================================================================


file = input('enter filename with extension: ')
split = file.split('.')[1]
print('the extension of the file is, ', split)
