"""
@Author: Swapnil Bhoyar
@Date: 2021-06-27 20:36:00 
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-06-26 20:37:00
@Title : Calculate wage of employee
"""

import random
print("Wellcome to employee wage computation")

def checkAttendance():
    """
    Description:
        This function determine if employee is present or absent
    """
    
    isPresent = 1
    attendance = random.randint(0,1)
    if attendance == isPresent:
        print("Employee is present")
    else:
        print("Employee is absent")

checkAttendance()