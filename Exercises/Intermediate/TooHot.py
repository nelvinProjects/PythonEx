"""Too Hot?

Given an integer value and a Boolean value, temperature and isSummer,
if temperature is between 60 and 90 (inclusive), unless its summer
where the upper limit is 100 instead of 90. Return true if the
temperature falls within the range, false otherwise.
"""


def too_hot(temperature: int, isSummer: bool) -> bool:
    if (isSummer and (temperature >= 60) and (temperature <= 100)) \
            or ((temperature >= 60) and (temperature <= 90)):
        return True
    elif ((not isSummer) and (temperature < 60 or temperature > 90)) \
            or (isSummer and (temperature < 60 or temperature > 90)):
        return False


print(too_hot(80, False))
print(too_hot(100, False))
print(too_hot(100, True))
