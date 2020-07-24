#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 02:42:56 2020

@author: trendydice
"""

# =============================================================================
#  Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.
# =============================================================================

import calendar
month  = input('month: ')
year = input('year:')


print(calendar.month(int(year),int(month)))

