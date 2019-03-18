#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 16:59:15 2019

The person wants to make a down_payment for her/his dream home. The down payment is one fourth of the total cost.
How many months are necessary to take this home. The condition is that the salary is incresaing by the percantage 
of semi-annual raise.

"""



current_saving = 0    
r = 0.04   # return for the investment
month = 0
annual_salary = float(input("Please enter your annual salary:"))
monthly_salary = annual_salary / 12
portion_saved = float(input("Please enter the amount of your salary to save as a decimal:"))
total_cost = float(input("Please enter the your dream home cost:"))
portion_down_payment = total_cost * 0.25
saved_money = monthly_salary*portion_saved


while(current_saving <= portion_down_payment):
    current_saving = (current_saving + current_saving * 0.04/12) + saved_money
    month = month + 1
print("Number of months:" , month)     
    
    
