"""BlackJack

Given 2 integer values greater than 0,
return whichever value is closest to 21 without going over 21.
If they both go over 21 then return 0
"""


def jack(value1: int, value2: int) -> int:
    """
    Find the value closet 21 between two inputs
    :param value1: the first value
    :param value2: the second value
    :return: the bigger value closest to 21
    """
    if (value1 <= 0) and (value2 <= 0):
        return 0
    elif (value1 > 21) and (value2 > 21):
        return 0
    elif (value1 <= 21) and (value1 > value2 or value2 > 21):
        return value1
    elif value2 <= 21 and (value2 > value1 or value1 > 21):
        return value2


print(jack(0, 21))
print(jack(21, 0))
print(jack(5, 18))
print(jack(19, 5))
print(jack(-5, 5))
