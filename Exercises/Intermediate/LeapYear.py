"""Leap year

Given a year work out if it is a leap year or not
"""


def leap_year(year: int) -> bool:
    if (year % 4 == 0) or (year % 400 == 0) and (year % 100 != 0):
        return True
    else:
        return False


print("Not leap year ", leap_year(2014))
print("leap year ", leap_year(2016))
print("leap year ", leap_year(2020))
print("Not leap year ", leap_year(2019))
