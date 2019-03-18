#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 12:45:27 2019

@author: FD
"""

'''

İt is possible to use log by importing math, numpy or pylab modules. In this case we accepted log base as "2".

'''


#import math
#x = int(input("Enter the number:"))
#y = int(input("Enter the number:"))
#print("x**y" , x**y)
#print("log(x)= " , math.log(x,2))

import numpy as np
x = int(input("Enter the number:"))
y = int(input("Enter the number:"))
print("x**y" , x**y)
print("log(x)= " , np.log(x) / np.log(2))