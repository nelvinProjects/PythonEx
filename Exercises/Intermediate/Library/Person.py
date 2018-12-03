class Person(object):
    def __init__(self, id, name, sex, age):
        self._id = id
        self._name = name
        self._sex = sex
        self._age = age

    def to_string(self):
        return str("Id: " + self._id + " | Name: " + self._name + " | Sex: " + self._sex + " | Age: " + str(self._age))
