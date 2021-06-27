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
        This function determine if employee is present or absent and calculate wage
    """
    
    isPresent = 1
    dayHour = 0
    wagePerHour = 20

    attendance = random.randint(0,1)
    if attendance == isPresent:
        dayHour = 8
        print("Employee is present")
    else:
        print("Employee is absent")

    employeeWage = wagePerHour * dayHour
    print("Employee wage is:", employeeWage)

checkAttendance()