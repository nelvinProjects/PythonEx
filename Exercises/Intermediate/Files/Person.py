class Person:
    def __init__(self, name, occupation, age):
        self.name = name
        self.occupation = occupation
        self.age = age

    def to_string(self):
        return str(self.name + "," + self.occupation + "," + str(self.age))


people = [
    Person("James", "Doctor", 25),
    Person("Cathy", "Nurse", 25),
    Person("Minty", "None", 25),
    Person("Tom", "Surgeon", 25),
    Person("David", "Developer", 25)
]

file = open("people.csv", "w")
for i in people:
    file.write(i.to_string() + "\n")

file.close()

read_file = []

file = open("people.csv", "r")
line = file.read()
read_file.append(line)
print(read_file)
