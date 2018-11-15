class Animal(object):
    def __init__(self, name, species, ambition = "Unknown"):
        self.name = name
        self.species = species
        self.ambition = ambition


class Sparrow(Animal):
    def __init__(self, name, ambition):
        Animal.__init__(self, name, "Sparrow", ambition)
        self.canFly = True

    def println(self):
        print(self.name, self.species, self.ambition,
              "can fly: ", self.canFly, sep=' ')


sparrow = Sparrow("Bell","good friend")
sparrow.println()