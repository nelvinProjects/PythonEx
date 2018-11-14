import pandas

# Example 1
x = 0


def a_function():
    global x
    x = 5
    print(x)


a_function()

print(x, end='\n\n')

# Example 2

name = "James"
age = 24

print("My name is %s and I am %d years old" % (name, age), end='\n\n')

# Example 3
DataSet = [("James", 30), ("Joseph", 32), ("Jack", 34)]
df = pandas.DataFrame(data=DataSet,
                      columns=['Names', 'Age'])
# Prints in table format
print(df, end='\n\n')

# Write to CSV
df.to_csv("names_ages.csv", index='false', header='false')

sortedData = df.sort_values(["Age"], ascending=False)
print(sortedData, end='\n\n')
print("Age MAX ", df["Age"].max(), end='\n\n')
# total count, mean, max
print(df.describe(), end='\n\n')

# Key and value
dictionary = {"first": df["Age"].count(), 2: ["bla", "blu"]}
print(dictionary, end='\n\n')

# Separate
print(20, 5, 1990, sep="-", end='\n\n')

# Jump for loop
for i in range(0, 10, 2):
    print(i)

print('\n\n')
for letter in "python":
    if letter == 'y':
        pass
        print("pass y")
    print(letter)
