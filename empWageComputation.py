"""
@Author: Swapnil Bhoyar
@Date: 2021-06-27 20:36:00 
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-06-28 01:26:00
@Title : Calculate wage of employee
"""

import random
print("Wellcome to employee wage computation")

def calculateWage(attendanceStatus):
    """
    Description:
        This function calculate wage
    """
    
    dayHour = 0
    wagePerHour = 20

    if attendanceStatus == isFullTime:
        dayHour = 8
    elif attendanceStatus == isPartTime:
        dayHour = 4 
    else:
        print("Employee is absent")

    employeeWage = wagePerHour * dayHour
    print("Employee wage is:", employeeWage)


absent = 0
isFullTime = 1
isPartTime = 2

switcher = {
    0: absent,
    1: isFullTime,
    2: isFullTime,
}

attendance = random.randint(0,2)
attendanceStatus = switcher.get(attendance)
calculateWage(attendanceStatus)
