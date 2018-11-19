"""Unique Sum

Given 3 integer values, return their sum. If one value is the same as
another value, they do not count towards the sum. Aka only return the
sum of unique numbers given.
"""


def unique_sum(one: int, two: int, third: int) -> int:
    """
    Sum values if not equal
    :param one: the first value
    :param two: the second value
    :param third: the third value
    :return: sum value or unique value
    """
    if (one == two) and (two == third):
        return 0
    elif one == two:
        return third
    elif one == third:
        return two
    elif two == third:
        return one
    else:
        return one + two + third


print(unique_sum(1, 2, 3))
print(unique_sum(3, 3, 3))
print(unique_sum(1, 1, 2))
