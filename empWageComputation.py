"""
@Author: Swapnil Bhoyar
@Date: 2021-06-27 20:36:00 
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-06-28 03:34:00
@Title : Calculate wage of employee
"""

import random
print("Wellcome to employee wage computation")

def calculateHour(attendanceStatus):
    """
    Description:
        this function determine the work hours
    Parameter:
        attendanceStatus is used to determine work hour of employee
    Return:
        the functution return 8 or 4 or 0 value as work hour
    """
    if attendanceStatus == isFullTime:
        dayHour = 8
    elif attendanceStatus == isPartTime:
        dayHour = 4 
    else:
        dayHour = 0
    return dayHour

def calculateWage():
    """
    Description:
        this function calculate employee wage
    Return:
        this function return total employee wage of a month
    """
    dailyWageList = []
    wagePerHour = 20
    workingDays = 0
    totalWorkingHours = 0
    maximumWorkingDays = 20
    maximumWorkingHours = 100
    totalWage = 0
    wageInfo = {}
    while workingDays < maximumWorkingDays and totalWorkingHours < maximumWorkingHours:
        attendance = random.randint(0,2)
        attendanceStatus = switcher.get(attendance)
        workingHours = calculateHour(attendanceStatus)
        dailyWage = workingHours * wagePerHour
        dailyWageList.append(dailyWage)
        totalWage += dailyWage
        totalWorkingHours += workingHours
        workingDays += 1
        wageInfo[workingDays] = {
            "Daily Wage:" : dailyWage,
            "Total Wage:" : totalWage
        }
    return wageInfo
        

absent = 0
isFullTime = 1
isPartTime = 2

switcher = {
    0: absent,
    1: isFullTime,
    2: isFullTime,
}

print("Total employee wage for month is:",calculateWage())