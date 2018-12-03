import Item


class Book(Item.Item):
    def __init__(self, id, name, taken):
        super().__init__(name, id, taken)

    def to_string(self):
        return str("Book - ID:" + self._id + " | Name: " + self._name + " | Taken: " + str(self._taken))


class Magazine(Item.Item):
    def __init__(self, id, name, taken):
        super().__init__(name, id, taken)

    def to_string(self):
        return str("Magazine - ID:" + self._id + " | Name: " + self._name + " | Taken: " + str(self._taken))


class Newspaper(Item.Item):
    def __init__(self, id, name, taken):
        super().__init__(name, id, taken)

    def to_string(self):
        return str("Newspaper - ID:" + self._id + " | Name: " + self._name + " | Taken: " + str(self._taken))
