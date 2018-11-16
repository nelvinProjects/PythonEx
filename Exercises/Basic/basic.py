from functools import partial

# Hello World
print("Hello World")

# Assignment
world = "Hello World"
print(world)


# Parameters
def output(string):
    return string


print(output("hey"))


# Sum function
def sum(value1, value2, addOrNot):
    if value1 == 0:
        return value2
    elif value2 == 0:
        return value1
    elif addOrNot:
        return value1 + value2
    else:
        return value2 * value1


print(sum(2, 2, True))
print(sum(2, 4, False))
print(sum(2, 0, False))
print(sum(0, 4, False), end='\n\n')

# Recursion
for i in range(10):
    print(sum(i, 4, False))

# Lists
numbersToUse = range(2, 12)
for j in numbersToUse:
    print(sum(j, 5, False))

# Recursion/Lists
newList = []
value = input("Enter how big the list to be \n")
for i in range(int(value)):
    print(i)
    newList.append(i)

for j in range(len(newList)):
    value = newList[j] * 10
    newList[j] = value
    print(value)


# Partial
def multiply(x, y):
    return x * y


double = partial(multiply, 2)
triple = partial(multiply, 3)

print(double(4))
print(triple(4))
