#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 02:23:00 2020

@author: trendydice
"""

# =============================================================================
#  Write a Python program to display the examination schedule.
# (extract the date from exam_st_date). 
#
#  exam_st_date = (11, 12, 2014)
#  Sample Output : The examination will start from : 11 / 12 / 2014 
# 
# =============================================================================

import datetime

exam_st_date = (11, 12, 2014)
year = int(exam_st_date[-1])
month = int(exam_st_date[1])
day = int(exam_st_date[0])
print('The examination will start from: ', datetime.date(year,month,day))
print('The examination will start from:  %i / %i /%i'%exam_st_date)